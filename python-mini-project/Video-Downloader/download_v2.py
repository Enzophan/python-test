from pytube import YouTube

def getYTVid(URL):
    """Get Highest Quality Video from YT URL."""
    YT = YouTube(URL)
    try:
        print(f"Downloading Video: {YT.title}")
        YTVIDEO_FILE_PATH = YT.streams.filter(only_audio=False, progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print(f"Download Video Completed: {YTVIDEO_FILE_PATH}\n")
    except Exception as e:
        print(f"Error: {e}")

def getYTAudio(URL):
    """Get Highest Quality Audio from YT URL."""
    YT = YouTube(URL)
    try:
        YTAUDIO_FILE_PATH = YT.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download()
        print(f"Download Video Completed: {YTAUDIO_FILE_PATH}\n")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    print("Downloading Audio")
    getYTAudio('https://www.youtube.com/watch?v=kE57Cy1Lyj0')  # Tom MacDonald - Dont Look Down (uncensored).mp4
    # print("Downloading Video")
    # getYTVid('https://www.youtube.com/watch?v=8wNUjCcaGrM')  # Tom MacDonald - I Wish.mp4
 