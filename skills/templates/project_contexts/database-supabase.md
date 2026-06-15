# Template: Supabase Postgres for Laravel

[Supabase](https://supabase.com/) is a powerful open-source Firebase alternative backed by a robust Postgres database. It provides an excellent free tier suitable for Laravel applications.

## 1. Prerequisites
- Create a free account at Supabase.
- Create a new project.
- Obtain your database password (you set this during project creation).
- Ensure your environment has the Postgres PHP extension installed (`pdo_pgsql`).

## 2. Environment Variables (`.env`)
Go to your Supabase Project Settings -> Database. You will find your connection parameters.

```env
DB_CONNECTION=pgsql
DB_HOST=db.yourprojectid.supabase.co
DB_PORT=5432
DB_DATABASE=postgres
DB_USERNAME=postgres
DB_PASSWORD=your_secure_password
```

## 3. Connection Pooling & IPv4 (Critical)
Supabase provides two ways to connect: IPv6 (direct) and IPv4 (via Supavisor pooler). 
Many hosting providers (like Vercel, some Render tiers, Github Actions) do not support IPv6. Therefore, it is highly recommended to use the **Supavisor connection pooler (IPv4)**.

In Supabase Settings -> Database -> Connection Pooler, find your pooled connection string:

```env
# The port is usually 6543 for the pooler instead of 5432
DB_HOST=aws-0-us-east-1.pooler.supabase.com
DB_PORT=6543
DB_DATABASE=postgres
DB_USERNAME=postgres.yourprojectid
DB_PASSWORD=your_secure_password
```

## 4. Laravel Configuration
If migrating from SQLite/MySQL, ensure you clear your caches before migrating.

```bash
php artisan config:clear
php artisan migrate
```
