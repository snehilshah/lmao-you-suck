import os
import csv
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import glob
import music_tag

path = "E:\\demistify\\EDrive\\Original List\\Hindi\\"
songs = glob.glob(path + "*.mp3*")
final = []

for song in songs:
    try:
        mp3file = MP3(song, ID3=EasyID3)
        music = music_tag.load_file(song)   

        title = mp3file.get('title', ['Unknown'])[0]
        album = mp3file.get('album', ['Unknown'])[0]
        artist = mp3file.get('artist', ['Unknown'])[0]
        file_name = os.path.basename(song)
        duration = mp3file.info.length

        final.append([title, album, artist, file_name, duration])
    except Exception as e:
        print(f"Failed to get metadata for {song}: {e}")

# Write to CSV
with open(path + 'song_details.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'Album', 'Artist', 'File Name', 'Duration'])
    csvwriter.writerows(final)
