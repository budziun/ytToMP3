\# ytToMP3 - YouTube to MP3 Downloader



\## 🎵 Overview

\*\*ytToMP3\*\* is a powerful and user-friendly desktop application for downloading high-quality MP3 files from YouTube videos. Built with modern GUI and advanced features, it's the perfect tool for music enthusiasts and content creators.



---



\## 🚀 Version 2.0 - Major Update!



\### 🆚 What's New: v1.5 → v2.0



\#### \*\*v1.5 (Console-based)\*\*

\- ✅ Basic command-line interface

\- ✅ Single video download only

\- ✅ Fixed desktop download location

\- ✅ 192kbps MP3 quality

\- ✅ Simple error handling



\#### \*\*v2.0 (GUI Revolution)\*\*

\- 🎨 \*\*Complete GUI Interface\*\* - Modern dark theme with CustomTkinter

\- 📋 \*\*Playlist Support\*\* - Download entire playlists with preview window

\- 🖼️ \*\*Thumbnail Integration\*\* - Real album covers embedded in MP3 files

\- ⚡ \*\*Concurrent Downloads\*\* - Download multiple files simultaneously (2x faster)

\- 🎛️ \*\*Advanced Controls\*\* - Pause, resume, and cancel downloads

\- 📊 \*\*Real-time Progress\*\* - Individual progress bars for each file

\- 📁 \*\*Custom Download Paths\*\* - Choose your preferred download location

\- 📄 \*\*Batch Processing\*\* - Load URLs from text files

\- ⏰ \*\*Time Estimation\*\* - Smart download time prediction

\- 🔧 \*\*Robust Error Handling\*\* - Retry mechanism for failed downloads

\- 🎯 \*\*Selective Downloads\*\* - Choose specific videos from playlists

\- 💾 \*\*File Management\*\* - Automatic cleanup of temporary files



---



\## ✨ Key Features



\### 🎨 \*\*Modern User Interface\*\*

\- \*\*Dark Theme\*\*: Easy on the eyes with professional styling

\- \*\*Intuitive Layout\*\*: Logical flow from folder selection to download completion

\- \*\*Real-time Feedback\*\*: Live status updates and progress tracking



\### 🎵 \*\*High-Quality Audio\*\*

\- \*\*192kbps MP3\*\*: Crystal clear audio quality

\- \*\*Embedded Thumbnails\*\*: Album artwork automatically added to files

\- \*\*Proper Metadata\*\*: Clean, organized music library



\### 🚀 \*\*Advanced Download Features\*\*

\- \*\*Concurrent Processing\*\*: Download up to 2 files simultaneously

\- \*\*Smart Retry Logic\*\*: Automatic retry on failed downloads with anti-detection

\- \*\*Playlist Preview\*\*: See all videos before downloading

\- \*\*Selective Download\*\*: Choose specific tracks from playlists

\- \*\*Batch Processing\*\*: Process multiple URLs from text files



\### 🎛️ \*\*Complete Control\*\*

\- \*\*Pause/Resume\*\*: Control your downloads in real-time

\- \*\*Cancel Anytime\*\*: Stop downloads and clean up files automatically

\- \*\*Progress Tracking\*\*: Individual progress bars with speed and ETA

\- \*\*Error Recovery\*\*: Intelligent handling of network issues and blocks



\### 📁 \*\*Smart File Management\*\*

\- \*\*Custom Paths\*\*: Download to any folder you choose

\- \*\*Clean Filenames\*\*: Automatic removal of invalid characters

\- \*\*Temp Cleanup\*\*: Automatic removal of temporary files (webp, jpg, etc.)

\- \*\*No Duplicates\*\*: Smart handling of existing files



---



\## 📦 Installation \& Usage



\### Option 1: Ready-to-Use Executable

1\. Download the latest `ytToMP3\_v2.0.exe` from \*\*Releases\*\*

2\. Run the executable - no installation required!

3\. The app includes all dependencies (ffmpeg, libraries)



\### Option 2: Run from Source

Install dependencies

pip install customtkinter yt-dlp Pillow mutagen requests



Download ffmpeg and place in /ffmpeg/bin/ folder

Run the application

python main.py



---



\## 🎯 How to Use



1\. \*\*📁 Choose Download Folder\*\* - Select where your MP3s will be saved

2\. \*\*🔗 Paste YouTube URL\*\* - Single video or entire playlist

3\. \*\*⚙️ Configure Options\*\* - Enable playlist mode if needed

4\. \*\*📋 Preview Playlist\*\* (optional) - Select specific videos to download

5\. \*\*🎵 Click "POBIERZ MP3"\*\* - Start downloading with real-time progress

6\. \*\*🎛️ Control Downloads\*\* - Pause, resume, or cancel as needed



---



\## 🛠️ Technical Specifications



\### \*\*Core Technologies\*\*

\- \*\*GUI Framework\*\*: CustomTkinter (modern, dark theme)

\- \*\*Download Engine\*\*: yt-dlp (latest YouTube compatibility)

\- \*\*Audio Processing\*\*: FFmpeg (high-quality conversion)

\- \*\*Image Processing\*\*: Pillow (thumbnail handling)

\- \*\*Metadata\*\*: Mutagen (MP3 tag management)



\### \*\*Performance\*\*

\- \*\*Concurrent Downloads\*\*: Up to 2 simultaneous downloads

\- \*\*Audio Quality\*\*: 192kbps MP3 (optimal size/quality ratio)

\- \*\*Speed\*\*: 2x faster than v1.5 with concurrent processing

\- \*\*Memory Efficient\*\*: Smart caching and cleanup



\### \*\*Compatibility\*\*

\- \*\*OS\*\*: Windows 10/11 (exe), Cross-platform (source)

\- \*\*Python\*\*: 3.7+ (for source code)

\- \*\*Dependencies\*\*: All included in exe version



---



\## 🔧 Advanced Features



\### \*\*Anti-Detection Technology\*\*

\- Real browser user agents

\- Smart retry mechanisms  

\- Rate limiting compliance

\- YouTube terms-friendly approach



\### \*\*Error Recovery\*\*

\- \*\*HTTP 403 Bypass\*\*: Smart handling of blocked requests

\- \*\*Network Timeouts\*\*: Automatic retry with exponential backoff

\- \*\*Corrupted Downloads\*\*: Verification and re-download

\- \*\*File Conflicts\*\*: Intelligent duplicate handling



\### \*\*Developer Features\*\*

\- Extensive logging for troubleshooting

\- Modular architecture for easy expansion

\- Clean separation of UI and download logic

\- Full async support for responsive interface



---



\## 📋 Requirements



\### \*\*For EXE Version\*\* (Recommended)

\- Windows 10/11

\- 200MB free space

\- Internet connection



\### \*\*For Source Code\*\*

pip install customtkinter>=5.2.0 yt-dlp>=2023.9.24 Pillow>=10.0.0 mutagen>=1.47.0 requests>=2.31.0


---



\## 🎉 Why Upgrade to v2.0?



| Feature | v1.5 | v2.0 |

|---------|------|------|

| Interface | ❌ Console only | ✅ Modern GUI |

| Playlists | ❌ Single videos | ✅ Full playlist support |

| Progress | ❌ Basic text | ✅ Real-time progress bars |

| Controls | ❌ No control | ✅ Pause/Resume/Cancel |

| Thumbnails | ❌ No artwork | ✅ Embedded covers |

| Speed | ❌ Sequential | ✅ 2x faster (concurrent) |

| Error Handling | ❌ Basic | ✅ Advanced retry logic |

| File Management | ❌ Desktop only | ✅ Custom paths + cleanup |



---



\## 🤝 Support



\- \*\*🐛 Issues\*\*: Report bugs on GitHub

\- \*\*💡 Features\*\*: Suggest new features via GitHub Issues  

\- \*\*☕ Support\*\*: \[Buy me a coffee](https://buycoffee.to/budziun)

\- \*\*🌐 Website\*\*: \[budziun.pl](https://budziun.pl)



---



\## 📄 License



This project is open source. Feel free to contribute, fork, or suggest improvements!



---



\*\*Made with ❤️ by \[budziun](https://github.com/budziun)\*\*



\*Download high-quality music the smart way! 🎵\*



