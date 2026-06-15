# ENV Workflow

Use this exact promotion flow for environment variables.

## 1) Local (development)

1. Copy `.env.local.example` to `.env`.
2. Fill required local values:
   - DB
   - `SENDZEN_API_TOKEN`
   - AI keys (`OPENAI_API_KEY` and/or `GEMINI_API_KEY` and/or `OPENROUTER_API_KEY`)
3. Run and verify locally:
   - `php artisan key:generate`
   - `php artisan migrate`
   - `php artisan test --compact`
4. Confirm the app flow works end-to-end.

## 2) Promote to Staging

1. Start from `.env.staging.example` (do not copy local `.env` blindly).
2. Set staging-only values:
   - `APP_ENV=staging`
   - `APP_URL`
   - staging DB credentials
   - staging queue/cache/session settings
   - staging SendZen + AI keys
3. Deploy code to staging.
4. Run on staging:
   - `php artisan migrate --force`
   - `php artisan config:cache`
   - `php artisan route:cache`
   - `php artisan view:cache`
5. Validate critical paths on staging (auth, reminders, scheduler eligibility, send pipeline).

## 3) Promote to Production

1. Start from `.env.production.example`.
2. Set production-only values:
   - `APP_ENV=production`
   - `APP_DEBUG=false`
   - production DB credentials
   - production queue/cache/session settings
   - production SendZen + AI keys
3. Deploy code to production.
4. Run on production:
   - `php artisan migrate --force`
   - `php artisan config:cache`
   - `php artisan route:cache`
   - `php artisan view:cache`
5. Smoke test production and monitor logs/queues.

## Promotion Rules (Always)

- Never commit real secrets.
- Keep `.env.example` and `*.env.example` templates updated whenever new vars are introduced.
- Promote only after verification passes in the previous environment.
- If staging fails, fix and re-run staging before touching production.
