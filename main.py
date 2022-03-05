from tkinter.filedialog import *
import webbrowser as web
from geopy.geocoders import Nominatim

#
# @author Erwan
# Github: github.com/erwanx2z
#
def getValues(ggaCoordonates):
    latitudeValue = float(ggaCoordonates[17:19]) + float(ggaCoordonates[19:28]) / 60
    longitudeValue = float(ggaCoordonates[31:34]) + float(ggaCoordonates[34:43]) / 60

    print("")
    print("Valeur de la latitude: ", latitudeValue)
    print("Valeur de la longitude: ", longitudeValue)
    print("")

    print("")
    print("Addresse; ", Nominatim(user_agent="findLocation").reverse([latitudeValue, longitudeValue]))
    print("")

    zoom = 18
    instruction = 'https://www.openstreetmap.org/?mlat=' + str(latitudeValue) + '&mlon=' + str(
        longitudeValue) + '#map=' + str(zoom) + '/' + str(latitudeValue) + '/' + str(longitudeValue)
    web.open(instruction)

print("Tapez 1 pour ouvrir le fichier et trouver la chaine de caractère automatiquement.")
print("Tapez 2 pour insérer la chaine de caractère manuellement.")
inputNumber = input("Entez ici votre réponse: ")

if int(inputNumber) == 1:
    tkinterBuilder = Tk()
    filePath = askopenfilename(title="Ouvrez votre ficher contenant les coordonnées GPS",
                               filetypes=[('fichier texte', '.txt'), ('tous fichiers', '.*')])
    try:
        file = open(filePath)
    except Exception as e:
        tkinterBuilder.destroy()
        file.close()
        print("exception stack trace", e)
        quit()

    lines = file.read().split("\n")
    file.close()
    tkinterBuilder.destroy()

    ggaCoordonates = "null"
    for line in lines:
        if "GGA" in line:
            ggaCoordonates = line

    if ggaCoordonates.__eq__("null"):
        print("Votre fichier ne contient pas de lignes GGA")
        print("Il doit contentir les caractères \"GGA\" et faire 72 caractères")
        quit()

    getValues(ggaCoordonates)

elif int(inputNumber) == 2:
    ggaCoordonates = input("Entrez ici votre chaine de caractère: ")
    if "GGA" in ggaCoordonates and len(ggaCoordonates) == 72:
        getValues(ggaCoordonates)
    else:
        print("Votre chaine de caractère n'est pas valide !")
        print("Elle doit contentir les caractères \"GGA\" et faire 72 caractères")
        quit()
else:
    print("Merci de répondre un nombre égal à 1 ou 2.")
    quit()
