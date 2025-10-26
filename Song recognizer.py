import yt_dlp

ytdl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '-',       # salida a stdout
    'quiet': True,
    'noplaylist': True

}

with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
    str(ydl.download(['https://www.youtube.com/watch?v=WBhgmyPYSbQ&list=RDWBhgmyPYSbQ']))