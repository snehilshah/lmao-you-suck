from mutagen.mp3 import MP3  
from mutagen.easyid3 import EasyID3  
# import mutagen.id3  
# from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER  
import glob  


# Change album name to first 5 words of title

# TODO:Change path to folder here
filez = glob.glob("D:/UpdateMusic/yt-py/*.mp3")  

for file in filez:
    mp3file = MP3(file, ID3=EasyID3)
    title = mp3file['title']
    
    # INFO:Change number of words here
    new_album = title[0].split()[0:6]
    new_album = ' '.join(new_album)
    
    mp3file['album'] = [new_album]
    mp3file.save()  
    print('Successfully Changed: ', title[0])


# Change track number to blank
for file in filez:
    mp3file = MP3(file, ID3=EasyID3)
    mp3file['tracknumber'] = ['']
    mp3file.save()