# 🎥 Any Video Downloader (MP4 - Highest Quality)

This Python script uses [`yt_dlp`](https://github.com/yt-dlp/yt-dlp) to download YouTube (or other supported) videos in the **highest quality** available (video + audio merged into a single `.mp4` file).

---

## ✅ Features

- Downloads highest-quality video and audio
- Merges streams into `.mp4` using `ffmpeg`
- Simple command-line interface
- Downloads to your Windows Videos folder

---

## 🛠️ Requirements

- Python 3.7+
- `yt_dlp` library
- `ffmpeg` installed and available in system PATH

---

## 📦 Installation

### 1. Install `yt_dlp`

Open a terminal or command prompt and run:

```bash
pip install -U yt-dlp
```

### 2. Install ffmpeg
```bash
winget install "FFmpeg (Essentials Build)"
```

### 3. Add FFmpeg to PATH
- Find installation path 
```bash
e.g.
C:\Users\[user]\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1.1-essentials_build\bin
```
To add to PATH:
1. Press Win + S, search "Environment Variables"
2. Click "Edit the system environment variables"
3. Click Environment Variables...
4. Under System variables, find and edit Path
5. Click New, paste the path above
6. Click OK on all windows
7. Restart VS Code or your terminal

### 4. Test FFMPEG
To make sure FFmpeg is installed, run:
```bash
ffmpeg -version
```

## !! IMPORTANT !!
- Change download_dir to your desired directory folder