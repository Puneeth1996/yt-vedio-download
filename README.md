# YouTube Video Downloader

A Python-based YouTube video downloader with batch processing capabilities.

## Features

- Download individual YouTube videos
- Batch download from URL lists
- Video enrichment with metadata
- Automatic file organization

## Files

- `pydtyt.py` - Main YouTube downloader script
- `videos_enricher.py` - Video metadata enrichment tool
- `videos.txt` - List of YouTube URLs to download
- `downloads/` - Downloaded videos storage directory

## Requirements

```
yt-dlp
requests
```

## Installation

```bash
pip install yt-dlp requests
```

## Usage

### Single Video Download
```bash
python pydtyt.py
```

### Batch Download
Add YouTube URLs to `videos.txt` (one per line) and run the script.

### Video Enrichment
```bash
python videos_enricher.py
```

## Directory Structure

```
yt-video-download/
├── downloads/          # Downloaded videos
├── pydtyt.py          # Main downloader
├── videos_enricher.py # Metadata tool
├── videos.txt         # URL list
└── README.md          # This file
```

## License

MIT License