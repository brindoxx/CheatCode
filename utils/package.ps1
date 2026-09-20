# utils/package.ps1
# Builds CheatCode.zip ready for GitHub Releases & Web Store distribution
# Author: brindoxx

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$ZipPath = Join-Path $ProjectRoot "CheatCode.zip"

Write-Host "[INFO] Packaging CheatCode by brindoxx..." -ForegroundColor Cyan

# Remove old zip if exists
if (Test-Path $ZipPath) {
    Remove-Item $ZipPath -Force
    Write-Host "[INFO] Removed existing CheatCode.zip" -ForegroundColor Yellow
}

$ItemsToInclude = @(
    "manifest.json",
    "data",
    "scripts",
    "styles",
    "popup",
    "icons",
    "README.md",
    "LICENSE"
)

$TempDir = Join-Path $env:TEMP ("CheatCode_Bundle_" + [System.Guid]::NewGuid().ToString().Substring(0, 8))
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

try {
    foreach ($item in $ItemsToInclude) {
        $sourcePath = Join-Path $ProjectRoot $item
        if (Test-Path $sourcePath) {
            Copy-Item -Path $sourcePath -Destination $TempDir -Recurse -Force
        }
    }

    Compress-Archive -Path "$TempDir\*" -DestinationPath $ZipPath -CompressionLevel Optimal
    Write-Host "[SUCCESS] CheatCode.zip successfully generated at: $ZipPath" -ForegroundColor Green
    Write-Host "[SUCCESS] Ready for GitHub Releases and Load Unpacked installation!" -ForegroundColor Green
}
finally {
    if (Test-Path $TempDir) {
        Remove-Item $TempDir -Recurse -Force
    }
}
