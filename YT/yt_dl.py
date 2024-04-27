''' Code that will procure us the option to download from youtube '''
from pytube import YouTube
from pytube import Playlist

# Verify if the link is a youtube link
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

# Download the music from the link
def get_music(link) -> bool:
    ''' Download the music from a link \n
    Return True if it's downloaded \n
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
def get_music_from_playlist(link):
    ''' Download the musics from a playlist '''
    assert isinstance(link, str), 'link must be a string'
    playlist = Playlist(link)
    counter = 1
    for urls in playlist.video_urls:
        print(str(counter) + ' ' + urls + ' is downloading...')
        get_music(urls)
        print(str(counter) + ' ' + urls + ' is downloaded')
        counter += 1

# Get the vido of the link
def get_video(link) -> None:
    ''' Download the video from a link '''
    assert isinstance(link, str), 'link must be a string'
    yt = YouTube(link)
    print(yt.title + ' is downloading...')
    target_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Musics_Download'))
    video_file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(target_directory) # pylint: disable=line-too-long
    print(yt.title + ' is downloaded')
    return video_file

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

