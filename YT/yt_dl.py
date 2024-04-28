""" Code that will procure us the option to download from youtube """
import os
from pytube import YouTube
from pytube import Playlist


# Verify if the link is a youtube link
def verify_link(link: str) -> str | bool:
    """ Verify if the link is a string \n
    Return the link if it's a YouTube or a YouTube music link  \n
    Return False if it's not a YouTube or a YouTube music link"""

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


# Download the music from the link
def get_music(link) -> bool:
    """ Download the music from a link \n
    Return True if it's downloaded \n
    Return False if it's not"""

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

    target_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Musics_Download'))

    try:
        audio_file = yt.streams.filter(only_audio=True).first().download(target_directory)
    finally:
        print("Ce lien youtube n'est pas valide ou non reconnu")

    base = os.path.splitext(audio_file)[0]

    # Conversion du fichier audio en mp3
    try:
        os.rename(audio_file, base + '.mp3')
    except FileExistsError:
        value = 1
        while True:
            try:
                os.rename(audio_file, base + ' (' + str(value) + ') ' + '.mp3')
                break
            except FileExistsError:
                value += 1
                continue

    print(yt.title + ' is downloaded')
    return True


# Get the music playlist of the link
def get_music_from_playlist(link) -> bool:
    """ Download the musics from a playlist """
    try:
        isinstance(link, str)
    except AssertionError:
        print('link must be a link')
        return False
    playlist = Playlist(link)
    counter = 1
    counter_total = 1
    for urls in playlist.video_urls:
        print(str(counter) + ' ' + urls + ' is downloading...')
        counter_total += 1
        try:
            get_music(urls)
            counter += 1
        except AssertionError:
            print(f"The {counter_total} failed to download")

    print(f"Successfuly download {counter} musics over {counter_total}")
    return True


# Get the vido of the link
def get_video(link) -> bool:
    """ Download the video from a link """
    try:
        isinstance(link, str)
    except AssertionError:
        print("A Video link is needed")
        return False

    try:
        assert isinstance(verify_link(link), str)
    except AssertionError:
        print("Lien non valide")
        return False

    yt = YouTube(link)
    print(yt.title + ' is downloading...')

    target_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Video_Download'))
    try:
        video_file = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(target_directory)  # pylint: disable=line-too-long
    finally:
        print("Ce lien youtube n'est pas valide ou non reconnu")
    print(yt.title + ' is downloaded')
    return True


# Get the video playlist of the link
def get_video_from_playlist(link: str) -> None:
    """ Download the video from a playlist """
    assert isinstance(link, str), 'link must be a string'
    playlist = Playlist(link)
    counter = 0
    for urls in playlist.video_urls:
        print(str(counter) + ' ' + urls + ' is downloading...')
        get_video(urls)
        print(str(counter) + ' ' + urls + ' is downloaded')
        counter += 1
