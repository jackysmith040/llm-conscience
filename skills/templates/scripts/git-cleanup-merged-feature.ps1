# Delete a merged feature branch locally and on origin.
# Usage: .\scripts\git-cleanup-merged-feature.ps1 -Branch feat/ph6-001-deck-export
param(
    [Parameter(Mandatory = $true)]
    [string] $Branch
)

$ErrorActionPreference = 'Stop'

if ($Branch -in @('main', 'develop')) {
    Write-Error "Refusing to delete protected branch: $Branch"
}

Write-Host "Fetching and pruning remotes..."
git fetch origin --prune

Write-Host "Updating develop..."
git checkout develop
git pull origin develop

if (git show-ref --verify --quiet "refs/heads/$Branch") {
    Write-Host "Deleting local branch $Branch..."
    git branch -d $Branch
} else {
    Write-Host "Local branch $Branch not found (already deleted?)."
}

$remoteExists = git ls-remote --heads origin $Branch 2>$null
if ($remoteExists) {
    Write-Host "Deleting remote branch origin/$Branch..."
    git push origin --delete $Branch
} else {
    Write-Host "Remote branch origin/$Branch not found (already deleted?)."
}

Write-Host "Done. On develop at $(git rev-parse --short HEAD)."
