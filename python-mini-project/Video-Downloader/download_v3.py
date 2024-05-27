from pytube import YouTube


# dif(YouTube)

link = "https://www.youtube.com/watch?v=FM0JdcSThmE"
try:
    yt = YouTube(link)
    print(yt.title)
    title = yt.title
    YT_FILE_PATH =   yt.streams.filter(only_audio=False, progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print(f"Download Video Completed: {YT_FILE_PATH}\n")
    pass
except Exception as error:
    print(f"Error: {error}")
    pass