" This file is the main file of the project (and the only one) "
import os
from pytube import YouTube
from pytube import Playlist
from tkinter import *

RUNNING = True

BG_ENTRY_COULEUR = '#000000'
BG_COULEUR = '#8F8F8F'
FG_COULEUR = '#FFFFFF'

label_text = 'Welcome to the youtube downloader'
label_download = None

# window = Tk()
# window.title("Youtube downloader")
# window.geometry("720x480")
# window.minsize(480, 360)

# v_choose = IntVar()
# entry_var = StringVar()

def label_resizing(text:str)->str:
    if len(text) > 20:
        return text[:50] + '\n' + text[50:]

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
    # Actualisation of the label
    if label_download is not None:
        label_text = yt.title + ' is downloading...'
        label_download.config(text=label_resizing(label_text))
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

# # Create the main frame
# main_frame = Frame(window, bg=BG_COULEUR)
# main_frame.pack(expand=YES, fill=BOTH)

# # Create the title label
# label_title = Label(main_frame, text="Youtube downloader", font=("Arial", 40), bg=BG_COULEUR, fg=FG_COULEUR)
# label_title.pack()

# # Create the link entry
# link_entry = Entry(main_frame, font=("Arial", 20), bg=BG_COULEUR, fg=FG_COULEUR, textvariable= entry_var)
# link_entry.pack()

# # Create the choice button
# choice_music = Radiobutton(main_frame, text="Music", font=("Arial", 20), bg=BG_COULEUR, variable=v_choose, value=0)
# choice_video = Radiobutton(main_frame, text="Video", font=("Arial", 20), bg=BG_COULEUR, variable=v_choose, value=1)
# choice_music_playlist = Radiobutton(main_frame, text="Music playlist", font=("Arial", 20), bg=BG_COULEUR, variable=v_choose, value=2)
# choice_video_playlist = Radiobutton(main_frame, text="Video playlist", font=("Arial", 20), bg=BG_COULEUR, variable=v_choose, value=3)
# choice_music.pack()
# choice_video.pack()
# choice_music_playlist.pack()
# choice_video_playlist.pack()

# # Create the button
# button = Button(main_frame, text="Download", font=("Arial", 20), bg=BG_COULEUR, fg=FG_COULEUR, command=button_action)
# button.pack()

# # Create label for the download
# label_download = Label(main_frame, text=label_text, font=("Arial", 20), bg=BG_COULEUR, fg=FG_COULEUR)
# label_download.pack()

# window.mainloop()

# Here is for cmd
while RUNNING :
    choose = int(input("Choisissez l'option \n"+
                    "0 - Arrêter le programme \n"+
                    "1 - Télécharger une musique \n"+
                    "2 - Télécharger une playlist de musique \n"+
                    "3 - Télécharger une vidéo \n"+
                    "4 - Télécharger une playlist de vidéo \n"))
    if choose == 0:
        RUNNING = False
    elif choose == 1:
        LINK = str(input("Entrez le lien de la musique : "))
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        print("Current working directory:", os.getcwd())
        print("hey")
        try:
            file_path = get_music(LINK)
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
    elif choose == 5:
        try:
            get_music(a)
        except:
            print("Erreur")

input("Appuyez sur une touche pour quitter")