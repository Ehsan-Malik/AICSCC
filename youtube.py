from pytube import YouTube
video_link='https://www.youtube.com/watch?v=0aiAfzA7hUM'
video=YouTube(video_link)
video.streams.filter(res='720p').first().download('D:\\Project')