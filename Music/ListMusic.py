from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import glob
import music_tag


songs = glob.glob("D:/UpdateMusic/yt-py/*.mp3*")
final = []

for song in songs:
    try:
        mp3file = MP3(song, ID3=EasyID3)
        music = music_tag.load_file(song)
        final.append(mp3file['title'][0])
    except:
        print(f"Failed to get metadata for {song}")

with open('./Music/Scraped-YT.md', 'a', encoding="utf-8") as file:
    file.write(f"# Scraped-YT \n\n")
    for song in final:
        file.write(f"1. {song}\n")
    file.close()
