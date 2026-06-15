# Template: Vercel Laravel Deployment

This template outlines the constraints, configuration, and architecture necessary to deploy a Laravel application to Vercel's Serverless Edge Network using the `vercel-community/php` runtime.

## Resources & Links
- **Vercel PHP Community Repo:** [https://github.com/vercel-community/php](https://github.com/vercel-community/php)
- **Vercel Laravel Example:** [https://github.com/contributte/vercel-examples/tree/master/php-laravel](https://github.com/contributte/vercel-examples/tree/master/php-laravel)

## 1. Core Serverless Constraints (The Reality of Vercel)
- **Read-Only Filesystem:** The entire application is read-only except for `/tmp`. Standard SQLite databases (`database.sqlite`) **cannot be used** because they require write access to the directory.
- **No Background Daemons:** You **cannot** run `php artisan queue:work`. All jobs must be processed synchronously (`QUEUE_CONNECTION=sync`) or triggered via HTTP webhooks to external services (like AWS SQS or Upstash Redis).
- **No Native Minutely Cron:** You **cannot** run `php artisan schedule:work`. Vercel Cron on the free tier only allows 1 run per day. 
  - **Solution:** Create an API route in Laravel (`routes/api.php`) that runs `Artisan::call('schedule:run')`. Then, sign up for [cron-job.org](https://cron-job.org/) (100% free) and set it to send an HTTP GET request to `https://your-vercel-app.com/api/run-scheduler` every minute. Secure this route with a bearer token or secret header!
- **Cold Starts & Timeouts:** Serverless functions sleep when idle. The first request takes a few seconds (Cold Start). Vercel Free Tier has a strict **10-second timeout** for all requests.

## 2. Runtime version (IMPORTANT — format changed)

> [!IMPORTANT]
> **Agent directive — DO NOT GUESS the runtime version or PHP mapping.** The `vercel-php` version ↔ PHP version mapping changes over time and the table below WILL go stale. Before writing `vercel.json`, fetch the current mapping from the source — [https://github.com/vercel-community/php](https://github.com/vercel-community/php) (README "Available PHP versions") — and pin the runtime that ships the project's exact PHP version. Never assume `@0.9.0` (or any version) is correct; confirm it. The same applies to Node.js version and supported PHP range.

> [!WARNING]
> **Breaking change:** Older guides use the legacy `vercel.json` `version: 2` + `builds` array with `"use": "vercel-community/php"`. This is **deprecated**. The current runtime is published as **`vercel-php@0.9.0`** and is wired up via the modern `functions` property with a `runtime` key. Using the old `builds` format with the new runtime will fail.

- **Current runtime:** `vercel-php@0.9.0`
- **PHP version is fixed per runtime release** — it is NOT selectable independently. Pick the runtime version that ships your target PHP. **Snapshot as of 2026-05 — verify against the repo before using (see Agent directive above):**

  | Runtime | PHP |
  |---------|-----|
  | `vercel-php@0.9.0` | 8.5.x |
  | `vercel-php@0.8.0` | 8.4.x |
  | `vercel-php@0.7.4` | 8.3.x |
  | `vercel-php@0.6.2` | 8.2.x |
  | `vercel-php@0.5.5` | 8.1.x |

- **For this project, use `vercel-php@0.8.0` (PHP 8.4)** to match the Render stack (`serversideup/php:8.4-fpm-nginx`). Swap the runtime string in `vercel.json` accordingly.
- **Node.js:** 22.x required by the build image.
- The runtime runs `composer install` for you during the build.

## 3. Required Configurations

### A. `api/index.php`
Vercel only allows function entry-points inside the `api/` directory. Forward to Laravel's normal public entry-point:
```php
<?php
// Forward Vercel requests to Laravel's public/index.php
require __DIR__ . '/../public/index.php';
```

### B. `vercel.json` (verified Laravel + Vite pattern)

**Verified** on [asford-data](https://asford-data.vercel.app) — full project lock file: `project-plan/context/deployment-vercel.md`. Source discussion: [vercel-community/php#568](https://github.com/vercel-community/php/issues/568).

```json
{
    "version": 2,
    "framework": null,
    "installCommand": "npm ci",
    "buildCommand": "npm run build && mkdir -p dist",
    "outputDirectory": "public",
    "functions": {
        "api/index.php": {
            "runtime": "vercel-php@0.8.0"
        }
    },
    "routes": [
        { "src": "/build/(.*)", "dest": "/build/$1" },
        {
            "src": "/(.*\\.(?:css|js|mjs|png|jpg|jpeg|gif|svg|ico|ttf|woff|woff2|eot|otf|webp|avif|txt|json))$",
            "dest": "/public/$1"
        },
        { "src": "/(.*)", "dest": "/api/index.php" }
    ]
}
```

- **Do not** use legacy `builds` + `@vercel/static` on `public/**` — it often packages `public/` before Vite runs → **404** on `/build/assets/*` (`public/build` is gitignored).
- **`outputDirectory: public`** ships Vite output after `buildCommand`. Use **`functions`**, not `builds`, for PHP.
- **`framework: null`** + `mkdir -p dist` avoids Vercel treating the repo as a Vite SPA with wrong routes.
- Pin **`vercel-php@0.8.0`** for PHP 8.4 (or fetch current mapping — see §2). Node **22.x** in `package.json` `engines`.
- Optional `composer.json` → `scripts.vercel` with `npm ci` / `npm run build` is a **backup** only; browser assets still require `installCommand` / `buildCommand` above.
- Prefer secrets in the **Vercel Dashboard** (`APP_KEY`, `APP_URL`, DB). Minimum production: `APP_ENV=production`, `APP_DEBUG=false`, `CACHE_STORE=array`, `SESSION_DRIVER=cookie`, `QUEUE_CONNECTION=sync`, `LOG_CHANNEL=stderr`, `/tmp` cache paths (see deployment lock file).

### C. `.vercelignore`
Exclude the local `vendor/` so the runtime installs a clean set during build:
```
/vendor
```

### D. `composer.json` + `package.json` build hooks

**`package.json`** — Node 22, Vite on deploy:

```json
{
    "engines": { "node": "22.x" },
    "scripts": {
        "build": "vite build",
        "vercel-build": "vite build"
    }
}
```

**`composer.json`** — optional; runs during PHP runtime build (assets for the **browser** still need `buildCommand`):

```json
{
    "scripts": {
        "vercel": [
            "npm ci",
            "npm run build",
            "@php artisan package:discover --ansi"
        ]
    }
}
```

### E. `api/php.ini` (optional php.ini overrides)
Place a custom `api/php.ini` to override PHP settings (e.g. `memory_limit`, `ffi.enable`). It is consumed during build.

### F. `AppServiceProvider.php` (Tmp Storage Fix)
Since the deployed filesystem is read-only except `/tmp`, map Laravel's compiled views and caches to `/tmp` on Vercel:
```php
public function register(): void
{
    if (isset($_ENV['VERCEL'])) {
        $this->app->useStoragePath('/tmp/storage');
    }
}
```
Ensure the tmp subdirectories exist at boot (`/tmp/storage/framework/{views,cache,sessions}`) — create them in the same `register()` if `config:cache`/`view:cache` weren't pre-built.

## 4. Recommended SaaS Stack for Vercel Laravel
- **Database:** Neon, Supabase, or PlanetScale (serverless Postgres/MySQL). For Neon on Vercel, use the **pooled** (`-pooler`) endpoint for app queries — serverless functions open/close connections constantly (see `database-neon.md`).
- **Cache / Sessions:** Upstash Redis (or `array`/`cookie` for stateless).
- **Queues:** Upstash QStash or SQS via HTTP webhooks (no persistent `queue:work` on serverless).
