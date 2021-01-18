import os, re, glob
from moviepy.editor import *

print("##== Converter To Mp3 ==##")
print("-- Version 1.0 -- Développé par Maxime Lefebvre --")

# Config dossier où récupérer les vidéos et où mettre les mp3
dossierVideo = "VideoToConvert"
dossierMp3 = "Mp3File"
print("Veuillez à mettre vos fichiers à convertir dans le dossier " + dossierVideo + " !")
print("Le fichier mp3 seront dans le dossier " + dossierMp3 + " !")

# Confirmation à la conversion
inputConversion = input("Voulez-vous lancer la conversion ? (o/n) : ")

# Vérification de l'existance des dossiers
if not os.path.exists('./' + dossierVideo):
    os.makedirs('./' + dossierVideo)
if not os.path.exists('./' + dossierMp3):
    os.makedirs('./' + dossierMp3)

# Variable et verif conversion
goConvert = False
if inputConversion == "o":
    goConvert = True
else:
    goConvert = False

# On vérif la conversion et la prépare
if goConvert:

    # Récupération des fichiers vidéos
    listVideos = glob.glob(dossierVideo + "/*")

    # Conversion de chaque fichiers en mp3
    for video in listVideos:
        print("Conversion en cours : " + video)
        videoFile = r'./' + video
        video = video.replace(dossierVideo, "")
        mp3File = r'./' + dossierMp3 + video + '.mp3'

        # Conversion vidéo vers mp3
        videoclip = VideoFileClip(videoFile)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3File)
        audioclip.close()
        videoclip.close()

        try:
            os.remove(dossierVideo + "/" + video)
        except:
            print("Une erreur lors de la suppression d'un fichier est survenue !")

else:
    print("Vous avez refusé la conversion des fichiers vidéos !")