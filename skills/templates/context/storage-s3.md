# Template: AWS S3 Storage for Laravel

Amazon S3 is the industry standard for object storage. When deploying Laravel to ephemeral servers or serverless environments (like Vercel or standard Render Web Services), you must store file uploads externally.

## 1. Prerequisites
- Create an AWS account.
- Create an S3 Bucket (ensure it has the correct public access policies if you want users to view images directly).
- Create an IAM User with programmatic access and attach an S3 policy granting full access to your new bucket.
- Install the AWS S3 Flysystem adapter for Laravel:
  ```bash
  composer require league/flysystem-aws-s3-v3 "^3.0"
  ```

## 2. Environment Variables (`.env`)
Laravel already has the `s3` disk configured in `config/filesystems.php`. You just need to provide the environment variables:

```env
FILESYSTEM_DISK=s3

AWS_ACCESS_KEY_ID=your_iam_access_key
AWS_SECRET_ACCESS_KEY=your_iam_secret_key
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=your_bucket_name
AWS_USE_PATH_STYLE_ENDPOINT=false
```

## 3. Code Modifications
When using the Storage facade, you can either rely on the default disk or specify the `s3` disk.

```php
// If FILESYSTEM_DISK=s3 is set, this uploads to S3
Storage::put('avatars/1.jpg', $fileContents);

// Retrieve public URL (Bucket must have public read access)
$url = Storage::url('avatars/1.jpg');

// Or use a temporary signed URL for private buckets
$url = Storage::temporaryUrl('avatars/1.jpg', now()->addMinutes(5));
```

## 4. Serving Files
If you are generating AI images or saving user uploads that should be publicly visible, ensure your S3 bucket has a `Bucket Policy` that allows `s3:GetObject` for `*` (everyone) on `arn:aws:s3:::your_bucket_name/*`.
