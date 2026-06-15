# Methodology: Render Free-Tier External Cron Pattern

**Applies to:** Laravel apps on Render free-tier web services using the `serversideup/php` Docker image.
**Problem solved:** OOM kills and double-dispatch bugs caused by running persistent background workers alongside the web server on a memory-constrained container.

---

## The Core Pattern

On Render's free plan (512MB RAM, 0.1 vCPU), a single web container must serve HTTP traffic. Running additional long-lived processes (`schedule:work`, `queue:work`) alongside nginx + php-fpm exhausts available memory and causes OOM kills, repeated container restarts, and failed health checks.

**Solution:** Expose a single secure HTTP endpoint that runs both the scheduler and queue worker synchronously on each call. Point an external free cron service (e.g. cronjob.org) at that endpoint on a per-minute interval.

```
cronjob.org (every minute)
    │
    └─► GET /cron-dispatch?key={CRON_TOKEN}
            │
            ├─ php artisan schedule:run      (emits queued jobs)
            └─ php artisan queue:work --stop-when-empty  (processes all jobs, then exits)
```

The container runs only: **nginx + php-fpm**. No persistent background workers.

---

## Implementation

### 1. The Endpoint (`routes/web.php`)

```php
Route::get('/cron-dispatch', function (Request $request) {
    $expectedToken = config('services.cron.token');
    $providedKey   = $request->query('key');

    // Resilient validation: handle '+' → space URL-decode bug in some web servers
    $isValid = $expectedToken && (
        $providedKey === $expectedToken ||
        str_replace(' ', '+', $providedKey) === $expectedToken ||
        urldecode($providedKey) === $expectedToken
    );

    if (! $isValid) {
        abort(403, 'Unauthorized.');
    }

    // 1. Programmatically execute the task scheduler (emits queued dispatch jobs)
    Artisan::call('schedule:run');
    $scheduleOutput = Artisan::output();

    // 2. Process queued jobs one at a time.
    //    NEVER use --stop-when-empty here: it calls Worker::stop() → exit($status)
    //    which terminates the PHP process mid-request. The Symfony response shutdown
    //    handler fires, tries to send a second HTTP response, and PHP throws
    //    "Cannot modify header information — headers already sent."
    //    --once uses runNextJob() which returns normally without exit().
    $queueOutput = '';
    $maxJobs = 200;
    for ($i = 0; $i < $maxJobs; $i++) {
        if (\DB::table('jobs')->count() === 0) {
            break;
        }
        Artisan::call('queue:work', ['--once' => true, '--sleep' => 0]);
        $queueOutput .= Artisan::output();
    }

    return response()->json([
        'status'          => 'success',
        'schedule_output' => $scheduleOutput,
        'queue_output'    => $queueOutput,
    ]);
});
```

### 2. Token Config (`config/services.php`)

```php
'cron' => [
    'token' => env('CRON_TOKEN'),
],
```

### 3. `render.yaml` — correct env var setup

```yaml
# ✅ Keep — runs php artisan migrate --force on deploy
- key: AUTORUN_LARAVEL_MIGRATION
  value: "true"

# ❌ Remove — persistent schedule:work competes with web server for RAM
# - key: AUTORUN_LARAVEL_SCHEDULER
#   value: "true"

# ❌ Remove — persistent queue:work races with /cron-dispatch endpoint
# - key: AUTORUN_LARAVEL_WORKER
#   value: "true"

# ✅ Required — without this the endpoint always returns 403
- key: CRON_TOKEN
  sync: false

# ✅ Route logs to Render's aggregator (not the persistent disk)
- key: LOG_CHANNEL
  value: stderr
- key: LOG_LEVEL
  value: warning
```

### 4. Mail port (Gmail SMTP)

| Port | Encryption | Correct? |
|------|-----------|---------|
| 465  | ssl       | ✅ SSL/TLS wrapping |
| 587  | tls       | ✅ STARTTLS (recommended) |
| 465  | tls       | ❌ Mismatch — likely fails |

Use port 587 + `tls` for maximum compatibility:

```yaml
- key: MAIL_PORT
  value: 587
- key: MAIL_ENCRYPTION
  value: tls
```

### 5. cronjob.org setup

1. Create a free account at cronjob.org.
2. Add a new cron job:
   - URL: `https://your-app.onrender.com/cron-dispatch?key=YOUR_TOKEN`
   - Schedule: every 1 minute
   - Method: GET
3. Set the same token value in Render Dashboard → Environment → `CRON_TOKEN`.

---

## Why Not `AUTORUN_LARAVEL_SCHEDULER` + `AUTORUN_LARAVEL_WORKER`?

The `serversideup/php` image uses S6-overlay to run these as supervised background processes within the container. On a free-tier Render plan:

| Process | Approx. RSS |
|---------|------------|
| nginx master + workers | ~30MB |
| php-fpm master + pool | ~80–120MB |
| `php artisan schedule:work` | ~50–80MB |
| `php artisan queue:work` | ~50–80MB |
| **Total** | **~210–310MB of 512MB** |

Under load (jobs running, AI calls in flight), the queue worker can spike to 150MB+. The container OOMs, the container restart loop begins, and Render marks the deploy as failed.

**Additional problem — double processing:** If both `AUTORUN_LARAVEL_WORKER` and the `/cron-dispatch` endpoint are active simultaneously, they compete for the same database queue rows. A job can be picked up by both workers at nearly the same time, causing duplicate sends (two birthday messages to the same person on the same day).

---

## Scheduler Constraints with This Pattern

Because `schedule:run` fires once per cron tick (not continuously), the scheduler granularity is limited to **once per minute**. Commands using `->everyMinute()` work perfectly. Commands using `->everySecond()` or sub-minute intervals are incompatible with this pattern.

`->onOneServer()` works correctly as long as `CACHE_STORE=database` (or Redis) is set — the database cache provides the atomic lock that prevents overlap.

---

## Database Backend Compatibility (Neon vs Turso)

This pattern relies on the `database` queue/cache drivers and a **read-after-write** drain check (`\DB::table('jobs')->count()` immediately after `schedule:run` emits jobs). The backend must return freshly-written rows synchronously.

- **Neon Postgres (default):** Fully synchronous. The drain check sees jobs the same request that queued them. ✅
- **Turso / libSQL:**
  - **Remote-only connection:** works — every query hits the remote primary, so the drain check is consistent. ✅
  - **Embedded replica connection:** ❌ **incompatible.** The local replica only syncs every `sync_interval` (default 300s). Jobs written to the remote primary by `schedule:run` won't appear in the local replica's `jobs` table until the next sync, so the drain loop sees `count() === 0` and exits without processing anything. If you use Turso for the queue, use a **remote-only** connection (no `database` file path, no `sync_interval`).
  - Also requires PHP **FFI + the native libSQL extension** in the container — see `production-laravel.md` § 7 Option B.

## Diagnostic Checklist (if cron dispatch is not firing)

1. **403 response from `/cron-dispatch`** → `CRON_TOKEN` env var is missing or doesn't match the `?key=` value in cronjob.org URL. Check Render Dashboard → Environment.
2. **`+` signs in token return 403** → URL-encode the token in the cronjob.org URL (replace `+` with `%2B`), or use the resilient three-way validation in the endpoint above.
3. **Jobs dispatched but not processed** → `QUEUE_CONNECTION` is not `database`. Check `render.yaml`.
4. **Scheduler runs but no jobs queued** → Check `schedule:run` output in the JSON response. Verify `->onOneServer()` is not blocking due to a stale lock (clear with `php artisan cache:clear`).
5. **Container OOM after adding workers back** → Remove `AUTORUN_LARAVEL_SCHEDULER` and `AUTORUN_LARAVEL_WORKER` from `render.yaml`. Never enable both patterns simultaneously.

---

## Real-World Incident Reference

### Incident 1 — Deploy failure + 403 on every cron call
**Project:** keepmybirthday (Laravel 13, Render free tier)
**Date:** 2026-05-20
**Symptoms:** Render deploy failed (health check timeout); all `/cron-dispatch` calls returned 403.
**Root causes:**
1. `AUTORUN_LARAVEL_SCHEDULER=true` + `AUTORUN_LARAVEL_WORKER=true` → OOM → container restart loop → deploy failure.
2. `CRON_TOKEN` absent from `render.yaml` → endpoint always aborted with 403.
3. `MAIL_PORT=465` + `MAIL_ENCRYPTION=tls` → mail misconfiguration (latent; would silently fail on first email send).
**Fix:** Removed both AUTORUN worker flags; added `CRON_TOKEN: sync: false`; corrected mail to port 587 + tls; added `LOG_CHANNEL: stderr` + `LOG_LEVEL: warning`.

### Incident 2 — "headers already sent" cascade on every web request
**Project:** keepmybirthday (Laravel 13, Render free tier)
**Date:** 2026-05-20
**Symptoms:** `PHP Fatal error: Cannot modify header information — headers already sent` in `Response.php:322` logged on every request; app returned 500.
**Root causes:**
1. `/cron-dispatch` called `Artisan::call('queue:work', ['--stop-when-empty' => true])`. This calls `Worker::stop()` → `exit($status)` mid-web-request. PHP's `HandleExceptions::handleShutdown()` fires, tries to render a second HTTP response after the first was committed, and `header()` fails.
2. `AppServiceProvider::boot()` called `Artisan::call('migrate')` on every production web request, racing with `AUTORUN_LARAVEL_MIGRATION` and breaking the migration state. Fix: guard with `! app()->isProduction() || app()->runningInConsole()`.
3. Health check path was `GET /` (default), which boots a full Laravel session. Changed `healthCheckPath` to `/up` (database-free endpoint) to decouple health probes from DB availability.
**Fix:** Replaced `--stop-when-empty` with `--once` loop (see code above); added `isProduction()` guard to self-healing migration; set `healthCheckPath: /up` in `render.yaml`.
