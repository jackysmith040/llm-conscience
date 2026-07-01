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

### A. `api/index.php` (With Static Asset Fallback)
Vercel only allows function entry-points inside the `api/` directory. 

By default, you could just require Laravel's public entry-point. However, when using Tailwind CSS v4 with vendor UI packages (like MaryUI), Vercel's Edge static builder fails to include the UI classes because it doesn't have `composer` installed to fetch the `vendor/` directory. 

To fix this CSS desync, use this advanced entrypoint. It intercepts missing static assets that fall through the Edge network and manually serves the correctly-built CSS from the PHP Lambda (which *does* run composer during its build):

```php
<?php

$uri = urldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));

// Vercel Edge Fallback: Serve static assets generated inside the PHP Lambda
if ($uri !== '/' && !str_contains($uri, '..')) {
    $publicPath = __DIR__ . '/../public' . $uri;
    if (file_exists($publicPath)) {
        $extension = pathinfo($publicPath, PATHINFO_EXTENSION);
        $mimeTypes = [
            'css' => 'text/css',
            'js'  => 'application/javascript',
            'svg' => 'image/svg+xml',
            'png' => 'image/png',
            'jpg' => 'image/jpeg',
            'jpeg'=> 'image/jpeg',
            'woff2'=> 'font/woff2',
            'woff'=> 'font/woff',
            'ttf' => 'font/ttf',
            'eot' => 'application/vnd.ms-fontobject',
        ];
        if (isset($mimeTypes[$extension])) {
            header('Content-Type: ' . $mimeTypes[$extension]);
            header('Cache-Control: public, max-age=31536000, immutable');
            readfile($publicPath);
            exit;
        }
    }
}

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
            "runtime": "vercel-php@0.9.0",
            "maxDuration": 60
        }
    },
    "routes": [
        {
            "src": "/(build/.*|hot|storage/.*|.*\\.(?:png|jpg|jpeg|gif|svg|ico|css|js|woff2?|eot|ttf|otf|mp4|webm|wav|mp3|m4a|aac|oga|webp|avif))$",
            "headers": { "cache-control": "public, max-age=31536000, immutable" },
            "continue": true
        },
        { "src": "^/$", "dest": "/api/index.php" },
        { "src": "^/index\\.php$", "dest": "/api/index.php" },
        { "handle": "filesystem" },
        { "src": "/.*", "dest": "/api/index.php" }
    ]
}
```

### The Ultimate Routing Rules Explained (ELI5)
- **Why `maxDuration: 60`?** By default, Vercel Serverless Functions time out after 10 seconds (or 15s on some tiers). For a Laravel app, especially one that processes queues (like sending emails or generating PDFs) over an HTTP trigger, 10 seconds is too short. Vercel Hobby tier allows setting `maxDuration` up to `60` seconds explicitly. (Pro tier allows up to 300s/900s depending on plan).
- **Why explicit `^/$` routing?** If you use `{ "handle": "filesystem" }`, Vercel naturally resolves the root `/` URL to `public/index.php`. Since Vercel doesn't associate `.php` files in `public/` with the PHP runtime, it literally **downloads your raw `index.php` source code**! Explicitly routing `/` and `/index.php` to `/api/index.php` BEFORE the filesystem check prevents this.
- **Why `{ "handle": "filesystem" }` instead of forced regex?** Livewire dynamically generates its `livewire.js` file via Laravel's router. If we force all `.js` requests to be served statically, Vercel looks for it on disk, fails, and returns a 404. `{ "handle": "filesystem" }` tells Vercel: *"Check if the file physically exists. If yes, serve it. If no, fall through to the next rule (the PHP backend)."*

- Pin **`vercel-php@0.9.0`** for PHP 8.5 (or fetch current mapping — see §2). Node **22.x** in `package.json` `engines`.
- Prefer secrets in the **Vercel Dashboard** (`APP_KEY`, `APP_URL`, DB). Minimum production: `APP_ENV=production`, `APP_DEBUG=false`, `CACHE_STORE=array`, `SESSION_DRIVER=cookie`, `QUEUE_CONNECTION=sync`, `LOG_CHANNEL=stderr`, `/tmp` cache paths.

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

**IMPORTANT (Laravel 13+):** Do not configure this inside `AppServiceProvider`. Do it directly in `bootstrap/app.php` **before** the `return $app;` statement. If placed incorrectly or after `$app` returns, Laravel boots the filesystem too early, triggering `tempnam(): file created in the system's temporary directory` crashes.

## 4. Common Vercel × Laravel Real-World Gotchas

### A. Neon Postgres SNI Routing & Laravel's `array_diff_key` Crash
- **The Issue:** Neon databases require Server Name Indication (SNI) to route connections. The Vercel PHP `libpq` client often fails with "Endpoint ID is not specified". If you follow Neon's default advice to add `?options=endpoint=<id>` to the URL, Laravel's `ConfigurationUrlParser` intercepts it and passes a String instead of an Array to the PDO config, triggering an `array_diff_key(): Argument #2 must be of type array, string given` fatal error.
- **The ELI5 Solution:** Neon allows you to bypass SNI by injecting the endpoint directly into the password! Change your `DATABASE_URL` password from `my_pass` to `endpoint=ep-your-id;my_pass`.

### B. HTTPS Mixed Content Errors on Vercel
- **The Issue:** Browsers block your Vite CSS/JS (`Mixed Content`) because Laravel generates `http://` asset links instead of `https://`.
- **The ELI5 Reason:** Vercel handles all secure HTTPS encryption at its front door (Edge/CDN) and forwards the request to your PHP app in plain unencrypted HTTP. Laravel natively assumes the site isn't secure.
- **The Solution:** Tell Laravel to explicitly trust Vercel's proxy headers. Add `$middleware->trustProxies(at: '*');` to your `bootstrap/app.php` file.

### C. "404 Not Found (from disk cache)" on Livewire
- **The Issue:** The browser refuses to load `livewire.js` even after you fixed the routing.
- **The ELI5 Reason:** If you ever deploy aggressive cache-control headers on a broken configuration, your browser caches the 404 failure locally and never asks the Vercel server for the file again.
- **The Solution:** Check the "Disable cache" box in DevTools Network tab and hard refresh.

### D. The `/api` Directory Routing Trap (404 Not Found)
- **The Issue:** You place your webhook or cron endpoints in `routes/api.php` (e.g. `/api/run-scheduler`) but Vercel immediately returns a raw `404 Not Found` before Laravel even boots.
- **The ELI5 Reason:** Vercel strictly reserves any URL starting with `/api/` for its own native Serverless Functions. It looks for a literal file like `api/run-scheduler.js`. If it doesn't find one, it throws a 404 and ignores your `vercel.json` rewrites. 
- **The Solution:** Move any webhooks, API routes, or HTTP scheduler triggers into `routes/web.php` and use `->withoutMiddleware(\Illuminate\Foundation\Http\Middleware\VerifyCsrfToken::class)` if they require POST requests. Hit them without the `/api` prefix (e.g. `/run-scheduler`).

## 4. Recommended SaaS Stack for Vercel Laravel
- **Database:** Neon, Supabase, or PlanetScale (serverless Postgres/MySQL). For Neon on Vercel, use the **pooled** (`-pooler`) endpoint for app queries — serverless functions open/close connections constantly (see `database-neon.md`).
- **Cache / Sessions:** Upstash Redis (or `array`/`cookie` for stateless).
- **Queues:** Upstash QStash or SQS via HTTP webhooks (no persistent `queue:work` on serverless).
