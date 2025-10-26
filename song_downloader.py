from io import BytesIO
from yt_dlp import YoutubeDL
import sys
from pydub import AudioSegment

class Song:
    def __init__(self):
        self.originalVideo = BytesIO()
        self.mp3Video = BytesIO()
        self.url: str

    def Url(self, url: str):
        """

        :type url: str
        """
        self.url = url

    def DownloadSong(self):
        original_stdout = sys.stdout
        sys.stdout = self.originalVideo

        ytdl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '-',
            'quiet': True,
            'noplaylist': True,
            'logtostderr': True,
        }

        with YoutubeDL(ytdl_opts) as ydl:
            ydl.download([self.url])

        sys.stdout = original_stdout
        self.originalVideo.seek(0)

    def SongIntoMP3(self):
        audio = AudioSegment.from_file(self.originalVideo, format="webm")
        audio.export(self.mp3Video, format="mp3")
        self.mp3Video.seek(0)

    def ReturnSong(self):
        return self.mp3Video

    def ReadSong(self):
        return self.mp3Video.read()

    def ClearBuffer(self):
        self.originalVideo.seek(0)
        self.mp3Video.seek(0)
        self.originalVideo.truncate(0)
        self.mp3Video.truncate(0)

