from yt_dlp import YoutubeDL
from pathlib import Path
from datetime import datetime
import shutil
import time

videos_file = Path("videos.txt")
if not videos_file.exists():
    print("videos.txt not found")
    raise SystemExit(1)

# Read lines, strip whitespace and ignore empty lines
with videos_file.open("r", encoding="utf-8") as f:
    raw_lines = [ln.rstrip("\n") for ln in f]

lines = [ln.strip() for ln in raw_lines if ln.strip()]

# Deduplicate while preserving order
seen = set()
unique = []
for ln in lines:
    if ln not in seen:
        seen.add(ln)
        unique.append(ln)

# If duplicates found, back up original and write cleaned file
if len(unique) != len(lines):
    backup_name = videos_file.with_name(f"videos_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    shutil.copy2(videos_file, backup_name)
    videos_file.write_text("\n".join(unique) + ("\n" if unique else ""), encoding="utf-8")
    print(f"Removed {len(lines) - len(unique)} duplicate(s). Backup saved to: {backup_name.name}")
else:
    print("No duplicates found. Proceeding with downloads.")

# Download using yt_dlp
ydl_opts = {
    'format': 'worst[ext=mp4]/worst',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'noplaylist': True,
    'extractor_retries': 3,
    'retries': 5,
    'sleep_interval': 10,
    'max_sleep_interval': 60,
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
    },
    'ignoreerrors': True,
    'no_warnings': False,
    'fragment_retries': 3,
    'skip_unavailable_fragments': True
}

with YoutubeDL(ydl_opts) as ydl:
    if unique:
        for url in unique:
            try:
                print(f"Downloading: {url}")
                ydl.download([url])
                print(f"Successfully downloaded: {url}")
            except Exception as e:
                print(f"Failed to download {url}: {str(e)}")
                continue
    else:
        print("No URLs to download.")
