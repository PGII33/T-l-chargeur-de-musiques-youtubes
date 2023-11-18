" This file is the main file of the project (and the only one) "
import os
from pytube import YouTube
from pytube import Playlist

RUNNING = True



def verify_link(link:str):
    ''' Verify if the link is a string \n
    Return the link if it's a youtube or a youtube music link '''
    assert isinstance(link, str), 'link must be a string'
    assert 'https://www.youtube.com/watch' in link or 'https://music.youtube.com/watch' in link, 'link must be a youtube link'
    if link[:29] == 'https://www.youtube.com/watch':
        return link
    if 'https://music.youtube.com/watch' in link:
        link = link.replace('music.', 'www.')
        if link[:29] == 'https://www.youtube.com/watch':
            return link

# Get The music of the link
def get_music(link):
    ''' Download the music from a link '''
    assert isinstance(link, str), 'link must be a string'
    try :
        verify_link(link)
    except :
        print('link must be a youtube link')
    yt = YouTube(link)
    print(yt.title + ' is downloading...')
    audio_file = yt.streams.filter(only_audio=True).first().download('Musics_Downloads')
    base = os.path.splitext(audio_file)[0]
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    print(yt.title + ' is downloaded')
    return new_file

# Get the vido of the link
def get_video(link) -> None:
    ''' Download the video from a link '''
    assert isinstance(link, str), 'link must be a string'
    yt = YouTube(link)
    print(yt.title + ' is downloading...')
    video_file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('Musics_Downloads') # pylint: disable=line-too-long
    print(yt.title + ' is downloaded')
    return video_file

# Get the music playlist of the link
def get_music_from_playlist(link):
    ''' Download the music from a playlist '''
    assert isinstance(link, str), 'link must be a string'
    playlist = Playlist(link)
    counter = 0
    for urls in playlist.video_urls:
        print(str(counter) + ' ' + urls + ' is downloading...')
        get_music(urls)
        print(str(counter) + ' ' + urls + ' is downloaded')
        counter += 1

# Get the video playlist of the link
def get_video_from_playlist(link:str) -> None:
    ''' Download the video from a playlist '''
    assert isinstance(link, str), 'link must be a string'
    playlist = Playlist(link)
    counter = 0
    for urls in playlist.video_urls:
        print(str(counter) + ' ' + urls + ' is downloading...')
        get_video(urls)
        print(str(counter) + ' ' + urls + ' is downloaded')
        counter += 1

print("Bienvenue dans le programme de téléchargement de musique et de vidéo \n")
# Here is for cmd
while RUNNING :
    choose = int(input("Choisissez l'option \n"+
                    "0 - Arreter le programme \n"+
                    "1 - Télécharger une musique \n"+
                    "2 - Télécharger une playlist de musique \n"+
                    "3 - Télécharger une vidéo \n"+
                    "4 - Télécharger une playlist de vidéo \n"))
    if choose == 0:
        RUNNING = False
    elif choose == 1:
        LINK = str(input("Entrez le lien de la musique : "))
        get_music(LINK)
    elif choose == 2:
        LINK = str(input("Entrez le lien de la playlist : "))
        get_music_from_playlist(LINK)
    elif choose == 3:
        LINK = str(input("Entrez le lien de la vidéo : "))
        print(LINK)
        get_video(LINK)
    elif choose == 4:
        LINK = str(input("Entrez le lien de la playlist : "))
        get_video_from_playlist(LINK)
    elif choose == 5:
        try :
            get_music(a)
        except :
            print("Erreur")

print(verify_link('https://music.youtube.com/watch?v=aUCxD1xX6fU'))