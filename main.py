import os
import youtube_dl
import moviepy.editor as moviepy

# cleaning files
try:
    os.remove("output.m4a")
except:
    pass


url = ""

# input url by user
while "youtube" not in url:
    url = input("Youtube link: ")
    if "youtube" not in url:
        print("Please enter youtube link.")

# options
ydl_opts = {
    "format":"bestaudio/best",
    "outtmpl" : "output.%(ext)s",
}

# download
youtube_dl.YoutubeDL(ydl_opts).download([url])

# m4a to mp3 convert
clip = moviepy.AudioFileClip("output.m4a")
clip.write_audiofile("output.mp3")
