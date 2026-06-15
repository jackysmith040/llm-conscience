# After develop was merged into main on GitHub: pull main and fast-forward develop.
# Usage: .\scripts\git-sync-develop-after-main-merge.ps1
$ErrorActionPreference = 'Stop'

Write-Host "Fetching and pruning remotes..."
git fetch origin --prune

Write-Host "Updating main..."
git checkout main
git pull origin main

Write-Host "Syncing develop with main..."
git checkout develop
git pull origin develop
git merge main
git push origin develop

Write-Host "Done. main and develop at $(git rev-parse --short main)."
