# Template: Neon Serverless Postgres for Laravel

[Neon](https://neon.tech/) is an excellent free-tier Serverless Postgres database. It scales to zero, branches like Git, and integrates perfectly with Laravel.

## 1. Prerequisites
- Create a free account at Neon.tech.
- Create a new project and database.
- Ensure your local machine or server has the Postgres PHP extension installed (`pdo_pgsql`).

## 2. Environment Variables (`.env`)
Neon provides a connection string. Break it down into your `.env` file:

```env
DB_CONNECTION=pgsql
DB_HOST=ep-example-word-123456.us-east-2.aws.neon.tech
DB_PORT=5432
DB_DATABASE=neondb
DB_USERNAME=your_neon_user
DB_PASSWORD=your_neon_password
```

## 3. Connection Pooling (Critical for Serverless/Vercel)
If you are deploying on a serverless platform (like Vercel) where connections constantly open/close, you **must** use Neon's pooled connection endpoint to avoid connection exhaustion.

In the Neon Dashboard, toggle the **"Pooled connection"** switch. It will add `-pooler` to the host name.

```env
# Notice the '-pooler' addition in the host for pooled connections
DB_HOST=ep-example-word-123456-pooler.us-east-2.aws.neon.tech
```

## 4. Laravel Configuration Optimization
If migrating from SQLite/MySQL, ensure your `config/database.php` has Postgres properly defined (it is by default in Laravel).

```bash
# Clear caches to apply changes
php artisan config:clear
php artisan migrate
```
