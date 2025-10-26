import os
import song_data


data = song_data.Data(os.getcwd())
data.GetSongDataFromYt('https://www.youtube.com/watch?v=WBhgmyPYSbQ&list=RDWBhgmyPYSbQ')
print(data.ReturnTitle(), data.ReturnAuthor(), data.ReturnImageUrl())
data.TitleFile()
data.AuthorFile()
data.ImageFile()
data.CurrentlySearchingSong()