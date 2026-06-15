# Template: Production Laravel Checklist

Use this template to ensure a Laravel application is fully hardened, optimized, and ready for a production environment, especially on ephemeral cloud hosts like Render.

> [!IMPORTANT]
> **Agent directive — DO NOT GUESS version-pinned values.** Any version number in this doc (PHP, base Docker image tag, Vercel runtime, Composer/NPM packages, driver versions) is a point-in-time snapshot and may be stale. Before pinning one in a config file, verify it against the authoritative source (the package/runtime repo or registry) and match the project's existing PHP version (`8.4` here). When unsure, fetch and confirm — never assume.

## 1. Environment Configuration
- `APP_ENV=production`
- `APP_DEBUG=false`
- `APP_KEY` is securely set.
- Log channel set to `errorlog` or `stderr` for Docker/cloud logging.

## 2. Optimization (Run during CI/CD or Docker build)
- `php artisan config:cache`
- `php artisan route:cache`
- `php artisan view:cache`
- `php artisan event:cache`
- Ensure `composer install --optimize-autoloader --no-dev` is used.

## 3. Storage & Database
- **SQLite on Ephemeral Hosts:** If using SQLite on services like Render, ensure the `database.sqlite` file is stored on a **Persistent Disk** mount.
- **File Uploads:** Map the `storage/app/public` directory to a Persistent Disk, or use S3/Cloudflare R2.
- Execute `php artisan storage:link`.

## 4. Queues & Scheduled Tasks
- **Queue Driver:** Ensure `QUEUE_CONNECTION` is set to `database` or `redis` (never `sync` in production).
- **Workers (paid/standard tier):** Configure a dedicated worker process (e.g., `php artisan queue:work --sleep=3 --tries=3`).
- **Scheduler (paid/standard tier):** Run `php artisan schedule:run` via cron or a dedicated worker container.
- **Free tier (Render / memory-constrained):** Do NOT run persistent workers in the web container. Use the external-cron pattern instead — see `render-external-cron-pattern.md`. Expose a secure `/cron-dispatch` endpoint and point cronjob.org at it. Enable only `AUTORUN_LARAVEL_MIGRATION`; never `AUTORUN_LARAVEL_SCHEDULER` or `AUTORUN_LARAVEL_WORKER` alongside the web server on 512MB RAM.
- **Serverless (Vercel):** No persistent processes at all. `QUEUE_CONNECTION=sync` (or push to Upstash QStash / SQS via HTTP), and trigger `schedule:run` from an external cron hitting a secured route. Filesystem is read-only except `/tmp`. See `vercel-laravel.md` — use `functions` + `outputDirectory: public` + Vite `buildCommand` (verified: [asford-data deployment-vercel.md](https://github.com/jackysmith040/asford-data/blob/main/project-plan/context/deployment-vercel.md)). Pin `vercel-php@0.8.0` for PHP 8.4; do **not** use legacy `builds` + `@vercel/static`.

## 5. Security & Proxies
- **Render (and most cloud hosts) terminate SSL at the load balancer** and forward plain HTTP to the container with `X-Forwarded-Proto: https`. Without trusting the proxy, Laravel generates `http://` asset URLs. Browsers block these as mixed content on the HTTPS page.
- In Laravel 11+, configure in `bootstrap/app.php`:
  ```php
  ->withMiddleware(function (Middleware $middleware): void {
      $middleware->trustProxies(at: '*');
      // ... other middleware
  })
  ```
- `at: '*'` trusts all proxies — correct for Render where the upstream IP is Render's own infrastructure.

## 6. Docker specific (ServerSideUp `serversideup/php:8.4-fpm-nginx`)

### ✅ Working Dockerfile pattern
```dockerfile
# Stage 1: build frontend assets
FROM node:20-alpine AS node_builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build
RUN test -d /app/public/build/assets || (echo "ERROR: Vite produced no assets" && exit 1)

# Stage 2: PHP image
FROM serversideup/php:8.4-fpm-nginx
ENV PHP_OPCACHE_ENABLE=1

# Add explicit NGINX rule so /build/ assets are served as static files,
# not passed to PHP (which would return 404 HTML with wrong Content-Type)
USER root
COPY docker/nginx-vite-assets.conf /etc/nginx/site-opts.d/10-vite-assets.conf

USER www-data
COPY --chown=www-data:www-data composer.json composer.lock ./
RUN composer install --no-dev --no-scripts --no-autoloader --prefer-dist
COPY --chown=www-data:www-data . .
COPY --chown=www-data:www-data --from=node_builder /app/public/build ./public/build
RUN test -d public/build/assets || (echo "ERROR: assets missing from final image" && exit 1)
RUN composer dump-autoload --optimize
RUN chmod -R 775 storage bootstrap/cache
```

**`docker/nginx-vite-assets.conf`:**
```nginx
location ^~ /build/ {
    access_log off;
    expires 1y;
    add_header Cache-Control "public, immutable";
    try_files $uri =404;
}
```

### ❌ Anti-patterns to avoid
- **Do not** run `composer run post-root-package-install` or `composer run post-create-project-cmd` at build time. These create a `.env` from `.env.example` (baking `APP_ENV=local`, `APP_DEBUG=true` into the image) and run `php artisan key:generate` without a real database, failing silently.
- **Do not** install `sqlite3` if you're using Postgres in production — dead weight.
- `bootstrap/cache/` in `.dockerignore` blocks the directory and breaks `composer dump-autoload` (package:discover needs to write there). Use `bootstrap/cache/*.php` instead to exclude only stale cached files while keeping the directory.

### Environment variables
- `AUTORUN_LARAVEL_MIGRATION=true` — safe on all plans; runs `migrate --force` once at container start.
- `AUTORUN_LARAVEL_SCHEDULER` / `AUTORUN_LARAVEL_WORKER` — **only enable on plans with sufficient RAM (1GB+)**. On free-tier (512MB), these persistent processes compete with nginx+php-fpm and cause OOM kills. Use the external-cron pattern instead (see `render-external-cron-pattern.md`).
- `PHP_OPCACHE_ENABLE=1` — enable in the Dockerfile `ENV` or `render.yaml`; disabled by default in the ServersideUp image.

## 7. Database choice

### Option A — Neon serverless Postgres (default, recommended)
Prefer a single `DB_URL` over 6 individual `DB_*` vars. Laravel's `pgsql` connector reads `env('DB_URL')` natively and parses host/port/database/user/password from it. Neon connection strings include `?sslmode=require`, making `DB_SSLMODE` redundant.

```yaml
# render.yaml — minimal DB config
- key: DB_CONNECTION
  value: pgsql
- key: DB_URL
  sync: false   # set in Dashboard: postgresql://user:pass@ep-xxx.neon.tech/db?sslmode=require
```

Use the **direct** Neon endpoint (`ep-xxx.neon.tech`), not the pooler (`ep-xxx-pooler.neon.tech`). PgBouncer transaction mode rejects session-level `SET` commands used by Laravel migrations.

### Option B — Turso / libSQL (SQLite at the edge)
Turso is a libSQL (SQLite fork) database. Attractive for free-tier edge apps: local-speed reads via **embedded replicas** that sync to a remote primary. **But it adds real production complexity — only choose it over Neon if you specifically want edge replicas.**

**Critical caveats (these decide whether it's viable for your host):**
- **FFI must be enabled** in PHP (`ffi.enable=true`). Many managed hosts disable FFI for security; verify your host allows it. The ServersideUp image allows it but it is not on by default.
- **Native libSQL extension must be installed into the Docker image.** It is *not* bundled with `serversideup/php`. You must add the libSQL extension binary + stub and load it via a custom `.ini`. This is the main reason it's heavier than Neon's "just set `DB_URL`" path.
- **Technical-preview status (as of early 2026).** The official `turso/libsql-laravel` SDK and the community `tursodatabase/turso-driver-laravel` are both young; an extension-free adapter was announced but not yet shipped. Less battle-tested than Postgres.

**Packages:** `composer require tursodatabase/turso-driver-laravel` (community, native extension) or `turso/libsql-laravel` (official SDK, preview).

**Connection modes** (`config/database.php`, driver `libsql`):
| Mode | Config keys | Use when |
|------|------------|----------|
| Remote-only | `url`, `password` (auth token) | simplest; every query hits the remote primary (network latency per query) |
| Local-only | `database` (file path) | dev / single-container; behaves like plain SQLite |
| Embedded replica | `database` + `url` + `password` + `sync_interval` | edge reads from a local file, periodic background sync to remote (default 300s) |

```env
DB_CONNECTION=libsql
TURSO_DATABASE_URL=libsql://your-db.turso.io
TURSO_AUTH_TOKEN=...
TURSO_SYNC_INTERVAL=300   # embedded replicas only
```

> [!WARNING]
> **Embedded replicas are eventually consistent.** A row written to the remote primary is not visible in the local replica until the next sync (`sync_interval`, default 5 min). This breaks any read-after-write logic — including the `/cron-dispatch` queue drain check (see `render-external-cron-pattern.md` § Turso). For `database` queue/cache/session on Turso, use a **remote-only** connection, not an embedded replica.

A dedicated step-by-step guide for the Neon path lives in `database-neon.md`; mirror it as `database-turso.md` if Turso becomes the primary choice.

## 8. Mail (Gmail SMTP)
- Port 587 + `MAIL_ENCRYPTION=tls` → STARTTLS ✅ (recommended)
- Port 465 + `MAIL_ENCRYPTION=ssl` → SSL/TLS wrapping ✅
- Port 465 + `MAIL_ENCRYPTION=tls` → **mismatch, will fail** ❌
