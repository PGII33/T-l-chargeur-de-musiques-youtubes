" This file is the main file of the project (and the only one) "
import os
from YT.yt_dl import get_music, get_music_from_playlist, get_video, get_video_from_playlist

if __name__ == "__main__":
    RUNNING = True

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
                FILE_PATH = get_music(LINK)
                assert FILE_PATH is not False
                print("Le fichier a été enregistré avec succès sous cette adresse : ", FILE_PATH)
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
