import contextlib
import wave
import speech_recognition as sr
import timeit
import os

import youtube_dl
import moviepy.editor as moviepy

# cleaning files
try:
    os.remove("output.%(ext)s")
except:
    pass


url = ""
type("")
while "youtube" not in url:
    url = input("Youtube link: ")
    if "youtube" not in url:
        print("Please enter youtube link.")

ydl_opts = {
    "format":"bestaudio/best",
    "outtmpl" : "output.%(ext)s",
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
clip = moviepy.AudioFileClip("output.m4a")
clip.write_audiofile("output.mp3")


print("Selam")