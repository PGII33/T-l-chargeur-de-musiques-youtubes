" This file is the main file of the project (and the only one) "
import os
from pytube import YouTube
from pytube import Playlist
from tkinter import *

RUNNING = True

def verify_link(link:str) -> str | bool:
    ''' Verify if the link is a string \n
    Return the link if it's a youtube or a youtube music link  \n
    Return False if it's not a youtube or a youtube music link'''

    # Vérification du type de la variable link
    try:
        isinstance(link, str)
    except AssertionError:
        print('Le lien doit être une chaîne de caractères')
        return False

    # Vérification du lien
    try:
        assert 'https://www.youtube.com/watch' in link or 'https://music.youtube.com/watch' in link
    except AssertionError:
        print('Le lien doit être un lien youtube ou youtube music')
        return False

    # Transformation du lien music en lien youtube
    try:
        assert link[:29] == 'https://www.youtube.com/watch' or 'https://music.youtube.com/watch' in link
        if link[:29] == 'https://www.youtube.com/watch':
            return link
        if 'https://music.youtube.com/watch' in link:
            link = link.replace('music.', 'www.')
            if link[:29] == 'https://www.youtube.com/watch':
                return link
    except AssertionError:
        print('Le lien doit être un lien youtube ou youtube music')
        return False

# Get The music of the link
def get_music(link) -> str | bool:
    ''' Download the music from a link \n
    Return the path of the music if it's downloaded \n
    Return False if it's not'''

    # Vérification du type de la variable link
    try:
        assert isinstance(link, str)
    except AssertionError:
        print('link must be a string')
        return False

    # Vérification du lien
    try:
        assert isinstance(verify_link(link), str)
    except AssertionError:
        print("Lien non valide")
        return False

    # Téléchargement de la musique
    yt = YouTube(link)
    print(yt.title + ' is downloading...')

    target_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Musics_Download'))
    audio_file = yt.streams.filter(only_audio=True).first().download(target_directory)
    base = os.path.splitext(audio_file)[0]
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    print(yt.title + ' is downloaded')
    if label_download != None:
        label_text = yt.title + ' is downloaded'
        label_download.config(text=label_resizing(label_text))
    return new_file

# Get the vido of the link
def get_video(link) -> None:
    ''' Download the video from a link '''
    assert isinstance(link, str), 'link must be a string'
    yt = YouTube(link)
    print(yt.title + ' is downloading...')
    if label_download != None:
        
        label_text = yt.title + ' is downloading...'
        label_download.config(text=label_resizing(label_text))
    target_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Musics_Download'))
    video_file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(target_directory) # pylint: disable=line-too-long
    print(yt.title + ' is downloaded')
    if label_download != None:
        label_text = yt.title + ' is downloading...'
        label_download.config(text=label_resizing(label_text))
    return video_file

# Get the music playlist of the link
def get_music_from_playlist(link):
    ''' Download the music from a playlist '''
    assert isinstance(link, str), 'link must be a string'
    playlist = Playlist(link)
    counter = 1
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

def button_action()-> None:
    ''' Get the link and the choice of the user and download the music or the video '''
    link = link_entry.get()
    if v_choose.get() == 0:
        get_music(link)
    elif v_choose.get() == 1:
        get_video(link)
    elif v_choose.get() == 2:
        get_music_from_playlist(link)
    elif v_choose.get() == 3:
        get_video_from_playlist(link)
    link_entry.delete(0, END)


print("Bienvenue dans le programme de téléchargement de musique et de vidéo \n")

# Here is for cmd
while RUNNING :
    choose = input("Choisissez l'option \n"+
                    "0 - Arrêter le programme \n"+
                    "1 - Télécharger une musique \n"+
                    "2 - Télécharger une playlist de musique \n"+
                    "3 - Télécharger une vidéo \n"+
                    "4 - Télécharger une playlist de vidéo \n")

    print("\n")

    try:
        choose = int(choose)
    except ValueError:
        print("Veuillez entrer un nombre valide")
        continue
    if choose == 0:
        RUNNING = False
    elif choose == 1:
        LINK = str(input("Entrez le lien de la musique : "))
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        try:
            file_path = get_music(LINK)
            assert file_path is not False
            print("Le fichier a été enregistré avec succès sous cette adresse : ", file_path)
        except AssertionError as e:
            print(e)
        except Exception as e:
            print("Une erreur imprévue s'est produite :", e)
        finally:
            os.chdir(os.path.abspath(os.curdir))
        print()
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
    else:
        print("Veuillez entrer un nombre valide")
        continue
