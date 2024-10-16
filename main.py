import yt_dlp
import os
import sys
import signal

def sigint_handler(signal, frame):
    print("\nPrzerwano program.")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def main():
    print("MP3 YT 1.3 by bdzn")
    link = input("Podaj link: ")

    download_path = os.path.join(os.path.expanduser("~"), "Desktop")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = os.path.join(script_dir, 'ffmpeg', 'bin')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,
        'quiet': False,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("\nZakończono pobieranie i konwersję do MP3\n")
    except Exception as e:
        print(f"Błąd podczas pobierania lub konwersji: {e}")

if __name__ == "__main__":
    main()
