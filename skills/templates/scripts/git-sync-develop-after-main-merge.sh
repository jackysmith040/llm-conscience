#!/bin/bash
# After develop was merged into main on GitHub: pull main and fast-forward develop.
# Usage: ./scripts/git-sync-develop-after-main-merge.sh

set -e

echo "Fetching and pruning remotes..."
git fetch origin --prune

echo "Updating main..."
git checkout main
git pull origin main

echo "Syncing develop with main..."
git checkout develop
git pull origin develop
git merge main
git push origin develop

echo "Done. main and develop at $(git rev-parse --short main)."
