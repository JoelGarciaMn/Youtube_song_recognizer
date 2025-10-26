from io import BytesIO
import sys
import yt_dlp
from shazamio import Shazam
import asyncio
from pydub import AudioSegment

def TestDownload():
    original_buffer = BytesIO()

    oldstdout = sys.stdout

    sys.stdout = original_buffer



    ytdl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '-',
        'quiet': True,
        'noplaylist': True,
        'logtostderr': True,
    }




    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=WBhgmyPYSbQ&list=RDWBhgmyPYSbQ'])

    sys.stdout = oldstdout

    original_buffer.seek(0)
    print(original_buffer.getvalue()[:16].hex(" "))


    audio = AudioSegment.from_file(original_buffer, format="webm")

    final_buffer = BytesIO()
    audio.export(final_buffer, format="mp3")
    final_buffer.seek(0)
    print(final_buffer.getvalue()[:16].hex(" "))
    final_buffer.seek(0)

    async def main(a):
        shazam = Shazam()

        out = await shazam.recognize(a)
        print(out)

    asyncio.run(main(final_buffer.read()))

class TestClass:
    def __init__(self, function):
        self.function = function.call()
    def use(self, message: str):
        self.function(message)

test = TestClass(print())
test.use("Hello World")
