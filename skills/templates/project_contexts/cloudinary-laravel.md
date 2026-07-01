# Template: Cloudinary Laravel Setup

This template outlines the installation, configuration, and best practices for integrating Cloudinary into a Laravel application using the official `cloudinary-labs/cloudinary-laravel` package.

## Resources & Links
- **Cloudinary Laravel Docs:** [https://laravel.cloudinary.dev/installation](https://laravel.cloudinary.dev/installation)
- **Cloudinary GitHub Repo:** [https://github.com/cloudinary-community/cloudinary-laravel/](https://github.com/cloudinary-community/cloudinary-laravel/)

## 1. Installation

Requires PHP 8.2+ and Laravel 11+.

```bash
composer require cloudinary-labs/cloudinary-laravel
```

## 2. Configuration

Run the artisan install command to set up the package configuration files:

```bash
php artisan cloudinary:install
```

Add your Cloudinary credentials to your `.env` file:

```dotenv
CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
CLOUDINARY_UPLOAD_PRESET=your_upload_preset
CLOUDINARY_NOTIFICATION_URL=
```

## 3. Core Features

### A. Blade Components
The package provides native Blade components for easy image and video rendering:

- **Image Component:**
  ```blade
  <x-cld-image public-id="sample" width="300" height="300" crop="fill" />
  ```
- **Video Component:**
  ```blade
  <x-cld-video public-id="sample_video" width="600" />
  ```
- **Upload Widget:**
  ```blade
  <x-cld-upload-button>Upload Image</x-cld-upload-button>
  ```

### B. File Storage Driver
Cloudinary can be used as a native Laravel storage disk. Once configured, you can use Laravel's standard Storage facade to interact with Cloudinary:

```php
use Illuminate\Support\Facades\Storage;

Storage::disk('cloudinary')->put('filename.jpg', $contents);
```

## 4. Best Practices & Optimization

- **Image Optimization:** Use Cloudinary's dynamic optimization by setting `fetch_format="auto"` (`f_auto`) and `quality="auto"` (`q_auto`) in your component attributes or fluent API calls to automatically serve the best format (like WebP/AVIF) and quality to users.
- **Upload Presets:** Secure uploads by defining Upload Presets in the Cloudinary dashboard and configuring `CLOUDINARY_UPLOAD_PRESET` in the `.env` file. This is particularly useful for applying transformations on upload.
