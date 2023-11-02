from pytube import YouTube
import os
import signal
import sys
def sigint_handler(signal, frame):
    print("\nPrzerwano program.")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

print("MP3 YT 1.1 by bdzn")
link = input("Podaj link: ")

try:
    yt = YouTube(link)

    if yt.streams:
        video = yt.streams.filter(only_audio=True).first()

        # Ustal ścieżkę do folderu "Downloads" na systemie Windows
        download_path = os.path.expanduser("~\Downloads")

        out_file = video.download(output_path=download_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print("\nZakończono Pobieranie\n")
    else:
        print("Nieprawidłowy link do filmu na YouTube.")
except Exception as e:
    print("Błąd podczas pobierania")
