from yt_dlp import YoutubeDL
from pathlib import Path
from datetime import datetime
import locale

# Set locale for date formatting (optional, for month names)
try:
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
except locale.Error:
    pass  # Fallback if locale not available

videos_file = Path("videos.txt")
if not videos_file.exists():
    print("videos.txt not found")
    raise SystemExit(1)

# Read URLs
with videos_file.open("r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

# yt-dlp options to extract info without downloading
ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    'extract_flat': False,
}

enriched_data = []

with YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        try:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'N/A')
            upload_date_str = info.get('upload_date', 'N/A')
            if upload_date_str != 'N/A':
                # Format date: 20251215 -> 2025 Dec 15
                dt = datetime.strptime(upload_date_str, '%Y%m%d')
                upload_date = dt.strftime('%Y %b %d')
            else:
                upload_date = 'N/A'
            view_count = info.get('view_count', 0)
            if view_count != 0:
                # Format views with commas
                views = f"{view_count:,}"
            else:
                views = 'N/A'
            duration_sec = info.get('duration', 0)
            if duration_sec:
                minutes = int(duration_sec // 60)
                seconds = int(duration_sec % 60)
                duration = f"{minutes} min {seconds} sec"
            else:
                duration = 'N/A'
            enriched_data.append({
                'URL': url,
                'Title': title,
                'Upload Date': upload_date,
                'Views': views,
                'Duration': duration
            })
        except Exception as e:
            print(f"Error processing {url}: {e}")
            enriched_data.append({
                'URL': url,
                'Title': 'Error',
                'Upload Date': 'Error',
                'Views': 'Error',
                'Duration': 'Error'
            })

# Generate timestamp for filename
timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
output_file = Path(f"BBall-{timestamp}.txt")

# Write to text file
with output_file.open("w", encoding="utf-8") as txtfile:
    txtfile.write("Enriched YouTube Videos Data\n")
    txtfile.write("=" * 50 + "\n\n")
    for item in enriched_data:
        txtfile.write(f"URL: {item['URL']}\n")
        txtfile.write(f"Title: {item['Title']}\n")
        txtfile.write(f"Upload Date: {item['Upload Date']}\n")
        txtfile.write(f"Views: {item['Views']}\n")
        txtfile.write(f"Duration: {item['Duration']}\n")
        txtfile.write("-" * 30 + "\n\n")

print(f"Enriched data saved to {output_file}")

# Clear the input file
with videos_file.open("w", encoding="utf-8") as f:
    f.write("")
print("Cleared videos.txt")