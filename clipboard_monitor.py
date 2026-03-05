import pyperclip
import time
import re
import os

# Function to check if text is a YouTube URL
def is_youtube_url(text):
    text = text.strip()
    # Patterns for YouTube URLs
    patterns = [
        r'https?://(www\.)?youtube\.com/watch\?v=[a-zA-Z0-9_-]+',
        r'https?://youtu\.be/[a-zA-Z0-9_-]+',
        r'https?://(www\.)?youtube\.com/shorts/[a-zA-Z0-9_-]+'
    ]
    for pattern in patterns:
        if re.match(pattern, text):
            return True
    return False

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
videos_file = os.path.join(script_dir, 'videos.txt')

# Initialize last clipboard
try:
    last_clipboard = pyperclip.paste()
except Exception as e:
    print(f"Error accessing clipboard: {e}")
    exit(1)

print("Clipboard monitor started. Copy YouTube links to add them to videos.txt. Press Ctrl+C to stop.")

try:
    while True:
        try:
            current = pyperclip.paste()
            if current != last_clipboard and current.strip():
                if is_youtube_url(current):
                    with open(videos_file, 'a', encoding='utf-8') as f:
                        f.write(current + '\n')
                    print(f"Added: {current}")
                last_clipboard = current
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Monitor stopped.")