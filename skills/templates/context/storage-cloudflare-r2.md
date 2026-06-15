# Template: Cloudflare R2 Storage for Laravel

[Cloudflare R2](https://www.cloudflare.com/developer-platform/r2/) is an S3-compatible object storage service with **zero egress fees**, making it highly cost-effective for SaaS applications deployed on Vercel or Render.

## 1. Prerequisites
- Create a Cloudflare account and navigate to R2.
- Create an R2 Bucket.
- Go to "Manage R2 API Tokens" and create a token with `Object Read & Write` permissions.
- You will receive an **Access Key ID**, **Secret Access Key**, and an **S3 API URL** (Endpoint).
- Ensure the AWS S3 adapter is installed in Laravel (R2 uses the exact same SDK):
  ```bash
  composer require league/flysystem-aws-s3-v3 "^3.0"
  ```

## 2. Environment Variables (`.env`)
Cloudflare R2 is 100% compatible with the S3 driver. You just configure the `s3` disk to point to the Cloudflare Endpoint.

```env
FILESYSTEM_DISK=s3

AWS_ACCESS_KEY_ID=your_cloudflare_access_key
AWS_SECRET_ACCESS_KEY=your_cloudflare_secret_key
# The region is usually 'us-east-1' or 'auto' for R2
AWS_DEFAULT_REGION=auto
AWS_BUCKET=your_r2_bucket_name
# This is critical! It points the AWS SDK to Cloudflare's servers
AWS_ENDPOINT=https://<YOUR_ACCOUNT_ID>.r2.cloudflarestorage.com
# Required for R2
AWS_USE_PATH_STYLE_ENDPOINT=true
```

## 3. Laravel Configuration Update
Ensure your `config/filesystems.php` reads the `AWS_ENDPOINT` variable. In modern Laravel versions, it does this automatically:

```php
's3' => [
    'driver' => 's3',
    'key' => env('AWS_ACCESS_KEY_ID'),
    'secret' => env('AWS_SECRET_ACCESS_KEY'),
    'region' => env('AWS_DEFAULT_REGION'),
    'bucket' => env('AWS_BUCKET'),
    'url' => env('AWS_URL'),
    'endpoint' => env('AWS_ENDPOINT'), // THIS MUST BE HERE
    'use_path_style_endpoint' => env('AWS_USE_PATH_STYLE_ENDPOINT', false), // AND THIS
    'throw' => false,
],
```

## 4. Serving Files (Public URLs)
R2 buckets are private by default. To serve images to your web application, go to your R2 Bucket settings in the Cloudflare Dashboard and configure a **Public.Dev subdomain** or attach a **Custom Domain**. 

Then update your `.env`:
```env
AWS_URL=https://pub-your-unique-id.r2.dev
```

When you call `Storage::url('avatars/1.jpg')`, Laravel will automatically prefix the image path with your Cloudflare Public URL!
