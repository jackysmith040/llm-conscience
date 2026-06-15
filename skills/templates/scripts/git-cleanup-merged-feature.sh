#!/bin/bash
# Delete a merged feature branch locally and on origin.
# Usage: ./scripts/git-cleanup-merged-feature.sh -b feat/ph6-001-deck-export

set -e

BRANCH=""
while getopts "b:" opt; do
  case $opt in
    b) BRANCH="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2; exit 1
    ;;
  esac
done

if [ -z "$BRANCH" ]; then
    echo "Usage: $0 -b <branch-name>"
    exit 1
fi

if [[ "$BRANCH" == "main" || "$BRANCH" == "develop" ]]; then
    echo "Refusing to delete protected branch: $BRANCH" >&2
    exit 1
fi

echo "Fetching and pruning remotes..."
git fetch origin --prune

echo "Updating develop..."
git checkout develop
git pull origin develop

if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
    echo "Deleting local branch $BRANCH..."
    git branch -d "$BRANCH"
else
    echo "Local branch $BRANCH not found (already deleted?)."
fi

if git ls-remote --heads origin "$BRANCH" | grep -q "$BRANCH"; then
    echo "Deleting remote branch origin/$BRANCH..."
    git push origin --delete "$BRANCH"
else
    echo "Remote branch origin/$BRANCH not found (already deleted?)."
fi

echo "Done. On develop at $(git rev-parse --short HEAD)."
