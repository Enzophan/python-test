from moviepy.editor import *

video = VideoFileClip("Hoa Bằng Lăng.mp4")

video.audio.write_audiofile("Hoa Bằng Lăng.mp3")


