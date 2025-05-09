import yt_dlp
import os 

# Define the download directory
# Make sure to replace with your actual username
download_dir = r"C:\Users\[yourusername]\Videos"

url = input("Enter the video URL: ")

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Tries best video+audio first, falls back to best single format
    'merge_output_format': 'mp4',
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    'noplaylist': True,
    'quiet': False,
    'progress_hooks': [
        lambda d: print(f"{d['_percent_str']} downloaded" if d['status'] == 'downloading' else "Download complete.")
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([url])
    except Exception as e:
        print(f"An error occurred: {e}")
