#!/bin/bash
#
# Simple bash script to download all Fortnite Icon Series videos
# Uses yt-dlp with best quality up to 4K
#

# Set directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$PROJECT_DIR/clips/raw"

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "========================================================"
echo "Fortnite Icon Series Video Downloader (Bash)"
echo "========================================================"
echo ""
echo "Output directory: $OUTPUT_DIR"
echo ""

# Check if yt-dlp is installed
if ! command -v yt-dlp &> /dev/null; then
    echo "❌ ERROR: yt-dlp is not installed!"
    echo ""
    echo "Install yt-dlp:"
    echo "  pip install yt-dlp"
    echo "  OR"
    echo "  sudo apt install yt-dlp"
    echo ""
    exit 1
fi

# Change to output directory
cd "$OUTPUT_DIR"

# Counter variables
SUCCESSFUL=0
FAILED=0

# Function to download video
download_video() {
    local filename="$1"
    local url="$2"

    # Skip if already exists
    if [ -f "$filename" ]; then
        echo "✅ Already exists: $filename"
        ((SUCCESSFUL++))
        return 0
    fi

    echo "⬇️  Downloading: $filename"
    echo "   URL: $url"

    if yt-dlp -f "best[height<=2160]" -o "$filename" "$url"; then
        echo "✅ Downloaded: $filename"
        echo ""
        ((SUCCESSFUL++))
        return 0
    else
        echo "❌ Failed: $filename"
        echo ""
        ((FAILED++))
        return 1
    fi
}

# Download all videos (add URLs as you find them)

# Ninja - January 17, 2020
download_video "01_Ninja_RealLife.mp4" "https://www.youtube.com/watch?v=BCn0O2oVuO4"
download_video "01_Ninja_Trailer.mp4" "https://www.youtube.com/watch?v=2kR5jnsM6eM"

# Loserfruit - June 22, 2020
download_video "02_Loserfruit_RealLife.mp4" "https://www.youtube.com/watch?v=3QzV1o1zE4k"
download_video "02_Loserfruit_Trailer.mp4" "https://www.youtube.com/watch?v=5zKqM7pK0zQ"

# Lachlan - November 13, 2020
# download_video "03_Lachlan_RealLife.mp4" "SEARCH: Lachlan PWR Fortnite"
download_video "03_Lachlan_Trailer.mp4" "https://www.youtube.com/watch?v=8fG5hJ2kL9M"

# TheGrefg - January 17, 2021
download_video "04_TheGrefg_RealLife.mp4" "https://www.youtube.com/watch?v=3eKqM7pK0zQ"
# download_video "04_TheGrefg_Trailer.mp4" "SEARCH: TheGrefg Icon Series Trailer"

# Add more as URLs are found...

# CouRageJD - December 17, 2025
download_video "13_CouRageJD_RealLife.mp4" "https://www.youtube.com/watch?v=f75_S-wRWHo"
# download_video "13_CouRageJD_Trailer.mp4" "CHECK: @Fortnite YouTube by Dec 15"

# Summary
echo ""
echo "========================================================"
echo "Download Summary"
echo "========================================================"
echo "✅ Successful: $SUCCESSFUL"
echo "❌ Failed: $FAILED"
echo ""
echo "📁 All downloads saved to: $OUTPUT_DIR"
echo ""
