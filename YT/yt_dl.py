import os
import yt_dlp

def _download_and_convert(youtube_url, output_directory, noplaylist):
    output_directory = os.path.abspath(output_directory)  # Convertir en chemin absolu
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Configuration des options de téléchargement
    ydl_opts = {
        'format': 'bestaudio',  # Télécharger le meilleur format audio disponible
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),  # Sauvegarder avec titre de vidéo
        'noplaylist': noplaylist,  # Télécharger une seule vidéo ou une playlist
        'postprocessors': [],  # Aucun post-traitement
        'nocheckcertificate': True,  # Ignorer les problèmes de certificat SSL
    }

    # Télécharger le fichier audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        if noplaylist:
            info = ydl.extract_info(youtube_url, download=False)
            title = info['title']
            ydl.download([youtube_url])
            # Construire le nom du fichier téléchargé
            downloaded_file = os.path.join(output_directory, f"{title}.webm")
        else:
            ydl.download([youtube_url])
            # Récupérer les chemins des fichiers téléchargés
            downloaded_files = [os.path.join(output_directory, file) for file in os.listdir(output_directory) if file.endswith('.webm')]
            downloaded_file = downloaded_files[0]

    # Vérifier si le fichier téléchargé existe
    if not os.path.exists(downloaded_file):
        raise FileNotFoundError(f"Le fichier téléchargé n'a pas été trouvé : {downloaded_file}")

    # Renommer le fichier en.mp3
    mp3_file = downloaded_file.rsplit('.', 1)[0] + '.mp3'
    os.rename(downloaded_file, mp3_file)
    print(f"Fichier renommé en : {mp3_file}")

    # Retourner le chemin du fichier MP3
    return mp3_file

def dl_music(youtube_url, output_directory):
    """
    Télécharge la musique à partir d'une URL et la sauvegarde le fichier audio dans le répertoire spécifié.
    Puis le fichier en.mp3.
    
    :param youtube_url: L'URL de la vidéo à télécharger.
    :param output_directory: Le répertoire où sauvegarder le fichier audio.
    :return: Le chemin complet du fichier avec l'extension.mp3.
    """
    return _download_and_convert(youtube_url, output_directory, True)

def dl_playlist(youtube_url, output_directory):
    """
    Télécharge une playlist de musiques à partir d'une URL et la sauvegarde les fichiers audio dans le répertoire spécifié.
    Puis les fichiers en.mp3.
    
    :param youtube_url: L'URL de la playlist à télécharger.
    :param output_directory: Le répertoire où sauvegarder les fichiers audio.
    :return: Les chemins complets des fichiers MP3.
    """
    # Télécharger la playlist
    mp3_file = _download_and_convert(youtube_url, output_directory, False)
    # Récupérer les chemins des fichiers téléchargés
    mp3_files = [os.path.join(output_directory, file) for file in os.listdir(output_directory) if file.endswith('.mp3')]
    return mp3_files