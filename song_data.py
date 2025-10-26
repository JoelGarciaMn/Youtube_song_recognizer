from shazamio import Shazam
import song_downloader
import asyncio
import os
import requests


async def RecognizeSong(MP3Song, processDuration: int = 12):
    shazam = Shazam(segment_duration_seconds=processDuration)
    out = await shazam.recognize(MP3Song)
    if "track" in out:
        track = out["track"]
        title = track.get("title")
        author = track.get("subtitle")
        imageUrl = track.get("images").get("coverart")
    else:
        title = "Unknown"
        author = "Unknown"
        imageUrl = "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/f0/b0/21/f0b021d2-8bfb-e2ff-93f9-17c64147f971/18UMGIM14845.rgb.jpg/400x400cc.jpg"

    return(title,
           author,
           imageUrl
           )

class Data:
    def __init__(self, directory):
        self.url: str
        self.title: str
        self.author: str
        self.imageUrl: str
        self.bigTitleFilePath = os.path.join(directory, "titleBig.txt")
        self.smallTitleFilePath = os.path.join(directory, "titleSmall.txt")
        self.bigAuthorFilePath = os.path.join(directory, "authorBig.txt")
        self.smallAuthorFilePath = os.path.join(directory, "authorSmall.txt")
        self.imageUrlFilePath = os.path.join(directory, "image.png")


    def GetSongDataFromYt(self, url):
        song = song_downloader.Song()
        song.Url(url= url)
        song.DownloadSong()
        song.SongIntoMP3()

        self.title, self.author, self.imageUrl = asyncio.run(RecognizeSong(song.ReadSong()))

        song.ClearBuffer()

    def ReturnTitle(self):
        return self.title

    def ReturnAuthor(self):
        return self.author

    def ReturnImageUrl(self):
        return self.imageUrl

    def TitleFile(self):
        if len(self.title) < 28:
            with open(self.smallTitleFilePath, "w", encoding="utf-8") as file:
                file.write(self.title)
        else:
            with open(self.bigTitleFilePath, "w", encoding="utf-8") as file:
                file.write(self.title + "  ")

    def AuthorFile(self):
        if len(self.author) < 28:
            with open(self.smallAuthorFilePath, "w", encoding="utf-8") as file:
                file.write(self.author)
        else:
            with open(self.bigAuthorFilePath, "w", encoding="utf-8") as file:
                file.write(self.author + "  ")

    def ImageFile(self):
        with open(self.imageUrlFilePath, "wb") as handle:
            response = requests.get(self.imageUrl, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

    def CurrentlySearchingSong(self):
        with open(self.bigTitleFilePath, "w") as file:
            file.write(" ")
        with open(self.smallAuthorFilePath, "w") as file:
            file.write(" ")
        with open(self.smallTitleFilePath, "w") as file:
            file.write(" ")
        with open(self.bigAuthorFilePath, "w") as file:
            file.write(" ")
        self.imageUrl = "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/f0/b0/21/f0b021d2-8bfb-e2ff-93f9-17c64147f971/18UMGIM14845.rgb.jpg/400x400cc.jpg"
        self.ImageFile()

