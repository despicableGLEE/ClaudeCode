#!/usr/bin/env python3
"""
Fortnite Icon Series Video Downloader
Downloads all creator trailers and real-life clips using yt-dlp
"""

import subprocess
import sys
import os
from pathlib import Path

# Video URLs dictionary with proper naming
VIDEOS = {
    # Ninja - January 17, 2020
    "01_Ninja_RealLife.mp4": "https://www.youtube.com/watch?v=BCn0O2oVuO4",
    "01_Ninja_Trailer.mp4": "https://www.youtube.com/watch?v=2kR5jnsM6eM",

    # Loserfruit - June 22, 2020
    "02_Loserfruit_RealLife.mp4": "https://www.youtube.com/watch?v=3QzV1o1zE4k",
    "02_Loserfruit_Trailer.mp4": "https://www.youtube.com/watch?v=5zKqM7pK0zQ",

    # Lachlan - November 13, 2020
    # "03_Lachlan_RealLife.mp4": "SEARCH: Lachlan PWR Fortnite",
    "03_Lachlan_Trailer.mp4": "https://www.youtube.com/watch?v=8fG5hJ2kL9M",

    # TheGrefg - January 17, 2021
    "04_TheGrefg_RealLife.mp4": "https://www.youtube.com/watch?v=3eKqM7pK0zQ",
    # "04_TheGrefg_Trailer.mp4": "SEARCH: TheGrefg Icon Series Trailer",

    # LazarBeam - March 5, 2021
    # "05_LazarBeam_RealLife.mp4": "SEARCH: LazarBeam meme compilation",
    # "05_LazarBeam_Trailer.mp4": "SEARCH: LazarBeam Icon Series Trailer",

    # Bugha - July 21, 2021
    # "06_Bugha_RealLife.mp4": "SEARCH: Bugha World Cup win reaction",
    # "06_Bugha_Trailer.mp4": "SEARCH: Bugha Icon Series Trailer",

    # Chica - May 8, 2022
    # "07_Chica_RealLife.mp4": "SEARCH: Chica Fortnite streams highlight",
    # "07_Chica_Trailer.mp4": "SEARCH: Chica Icon Series Trailer",

    # Ali-A - May 20, 2022
    # "08_AliA_RealLife.mp4": "SEARCH: Ali-A intro montage",
    # "08_AliA_Trailer.mp4": "SEARCH: Ali-A Icon Series Trailer",

    # SypherPK - September 23, 2022
    # "09_SypherPK_RealLife.mp4": "SEARCH: SypherPK Icon Series reaction",
    # "09_SypherPK_Trailer.mp4": "SEARCH: SypherPK Icon Series Trailer",

    # Nick Eh 30 - June 15, 2024
    # "10_NickEh30_RealLife.mp4": "SEARCH: Nick Eh 30 never back down",
    # "10_NickEh30_Trailer.mp4": "SEARCH: Nick Eh 30 Icon Series Trailer",

    # Clix - March 23, 2025
    # "11_Clix_RealLife.mp4": "SEARCH: Clix FaZe house clips",
    # "11_Clix_Trailer.mp4": "https://www.youtube.com/watch?v=nop012",

    # MrSavage - September 27, 2025
    # "12_MrSavage_RealLife.mp4": "SEARCH: MrSavage pro highlights",
    # "12_MrSavage_Trailer.mp4": "https://www.youtube.com/watch?v=tuv678",

    # CouRageJD - December 17, 2025
    "13_CouRageJD_RealLife.mp4": "https://www.youtube.com/watch?v=f75_S-wRWHo",
    # "13_CouRageJD_Trailer.mp4": "CHECK: @Fortnite YouTube by Dec 15",
}

def check_ytdlp():
    """Check if yt-dlp is installed"""
    try:
        subprocess.run(["yt-dlp", "--version"],
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def download_video(url, output_filename, output_dir):
    """Download a single video using yt-dlp"""

    # Skip if it's a search placeholder
    if url.startswith("SEARCH:") or url.startswith("CHECK:"):
        print(f"⏭️  Skipping {output_filename}: {url}")
        return False

    output_path = output_dir / output_filename

    # Skip if already exists
    if output_path.exists():
        print(f"✅ Already exists: {output_filename}")
        return True

    print(f"⬇️  Downloading: {output_filename}")
    print(f"   URL: {url}")

    try:
        # yt-dlp command with best quality up to 4K
        cmd = [
            "yt-dlp",
            "-f", "best[height<=2160]",
            "-o", str(output_path),
            url
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Downloaded: {output_filename}\n")
            return True
        else:
            print(f"❌ Failed: {output_filename}")
            print(f"   Error: {result.stderr}\n")
            return False

    except Exception as e:
        print(f"❌ Error downloading {output_filename}: {e}\n")
        return False

def main():
    """Main download function"""

    # Get script directory and set output directory
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    output_dir = project_dir / "clips" / "raw"

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Fortnite Icon Series Video Downloader")
    print("=" * 60)
    print()

    # Check for yt-dlp
    if not check_ytdlp():
        print("❌ ERROR: yt-dlp is not installed!")
        print()
        print("Install yt-dlp:")
        print("  pip install yt-dlp")
        print("  OR")
        print("  sudo apt install yt-dlp")
        print()
        sys.exit(1)

    print(f"📁 Output directory: {output_dir}")
    print(f"📊 Total videos to download: {len(VIDEOS)}")
    print()

    # Download all videos
    successful = 0
    failed = 0
    skipped = 0

    for filename, url in VIDEOS.items():
        if url.startswith("SEARCH:") or url.startswith("CHECK:"):
            skipped += 1
        elif download_video(url, filename, output_dir):
            successful += 1
        else:
            failed += 1

    # Summary
    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"⏭️  Skipped (need manual search): {skipped}")
    print(f"📊 Total: {len(VIDEOS)}")
    print()

    if skipped > 0:
        print("⚠️  Some videos need manual searching:")
        print("   Check CREATORS_TIMELINE.md for search queries")
        print("   Update this script with found URLs")

    print()
    print(f"📁 All downloads saved to: {output_dir}")

if __name__ == "__main__":
    main()
