from pytube import YouTube
import os
import signal
import sys
from moviepy.editor import AudioFileClip

def sigint_handler(signal, frame):
    print("\nPrzerwano program.")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

print("MP3 YT 1.2 by bdzn")
link = input("Podaj link: ")

try:
    yt = YouTube(link)

    if yt.streams:
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

        download_path = os.path.expanduser("~\Downloads")
        out_file = audio_stream.download(output_path=download_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"


        audio_clip = AudioFileClip(out_file)
        audio_clip.write_audiofile(new_file, codec="mp3", bitrate="192k")
        audio_clip.close()

        os.remove(out_file)

        print("\nZakończono Pobieranie i Konwersję do MP3\n")
    else:
        print("Nieprawidłowy link do filmu na YouTube.")
except Exception as e:
    print("Błąd podczas pobierania")
