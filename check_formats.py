from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=nC2b_ZfAeZg"

ydl_opts = {
    'listformats': True,
    'no_warnings': False
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])