# MP3 YT Downloader

### Description
This is a simple tool for downloading audio from YouTube videos and converting them to `.mp3` format. The program fetches audio streams from YouTube and uses `ffmpeg` for post-processing to convert them into high-quality `.mp3` files at `192 kbps` bitrate.

### Requirements
Before running the program, you need to install the following dependencies:
- **Required Python libraries:**
  - `yt-dlp` (for downloading videos)
  - `ffmpeg` (download via official page)

### Example Usage
```bash
MP3 YT 1.5 by bdzn
Enter the YouTube link: 'your YouTube link with video'
```

---

### How to Download

#### Option 1: Downloading the `.exe` file

1. Go to the **GitHub Releases** tab in this repository.
2. Download the latest `.zip` file, which contains the `.exe` application.
3. Extract the downloaded `.zip` file on your computer.
4. Run the extracted `.exe` file to use the application directly (no need for additional libraries or configuration).

#### Option 2: Installing from Source Code

1. Ensure you have **Python** and the required libraries (`yt-dlp`, `ffmpeg`) installed.
2. If needed, follow the steps below to install `ffmpeg`.

   ### How to Install `ffmpeg` on Windows
   - Download the `ffmpeg` build from the [official site](https://ffmpeg.org/download.html).
   - Extract the files and add the `bin` folder (e.g., `C:\ffmpeg\bin`) to your system's PATH environment variable.

3. Clone the repository and run the `main.py` source file.



