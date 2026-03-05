# YouTube Video Downloader

A Python-based YouTube video downloader with batch processing capabilities.

## Features

- Download individual YouTube videos
- Batch download from URL lists
- Video enrichment with metadata
- Automatic file organization
- Clipboard monitoring to automatically collect YouTube URLs

## Files

- `pydtyt.py` - Main YouTube downloader script
- `videos_enricher.py` - Video metadata enrichment tool
- `clipboard_monitor.py` - Clipboard monitor to automatically add YouTube URLs to videos.txt
- `videos.txt` - List of YouTube URLs to download
- `downloads/` - Downloaded videos storage directory

## Requirements

```
yt-dlp
requests
pyperclip
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Single Video Download

```bash
python pydtyt.py
```

### Batch Download

Add YouTube URLs to `videos.txt` (one per line) and run the script.

### Clipboard Monitor

Run the clipboard monitor to automatically add copied YouTube URLs to `videos.txt`:

```bash
python clipboard_monitor.py
```

The script will run continuously, monitoring the clipboard. Copy YouTube links from your browser, and they will be automatically added to `videos.txt`. Press Ctrl+C to stop the monitor.

### Video Enrichment

```bash
python videos_enricher.py
```

## Directory Structure

```
yt-video-download/
├── downloads/             # Downloaded videos
├── pydtyt.py             # Main downloader
├── videos_enricher.py    # Metadata tool
├── clipboard_monitor.py  # Clipboard monitor
├── videos.txt            # URL list
├── requirements.txt      # Dependencies
└── README.md             # This file
```

## License

MIT License
