import os
import YT.yt_dl

if __name__ == "__main__":
    RUNNING = True

    print("Bienvenue dans le programme de téléchargement de musique et de vidéo \n")

    while RUNNING:
        choose = input("Choisissez l'option\n" +
                       "0 - Arrêter le programme\n" +
                       "1 - Télécharger une musique\n" +
                       "2 - Télécharger une playlist de musique\n")

        print("\n")

        try:
            choose = int(choose)
        except ValueError or choose > 2 or choose < 0:
            print("Veuillez entrer un nombre entre 0 et 2")
            continue

        match choose:
            case 0: #Exit the program
                exit()
            case 1: # Download a music
                link = input("Lien de la musique youtube : ")
                YT.yt_dl.dl_music(link, "./Musiques")
                continue
            case 2: # Download a playlist
                link = input("Lien de la playlist youtube : ")
                YT.yt_dl.dl_playlist(link, "./Musiques")
            case default: # Reask for a valid number
                print("Invalid Error")
                exit()
