# TP Zcasino roulette :

from random import randrange
from math import ceil

argent = 1000
continuer_partie = True

print("Vous vouys installez a la table de roulette avec ", argent, "$.")


while continuer_partie:
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) :")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Vous n'avez pas choisit de nombre'")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            ("Le nombre choisit est négatif")
        if nombre_mise > 49: 
            print("Le nombre choisit est supérieur  49.")
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise :")

        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas entrer de nombre.")
            mise = -1
            continue
        if mise == 0:
            print("Votre mise est nulle.")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$.")


    numero_gagnant = randrange(50)
    print("La roulette tourne...et le numéro gagnant est :", numero_gagnant)

    if numero_gagnant == nombre_mise:
        print("Félicitation ! Vous avez gagné :", mise * 3,"$ !")
        argent += mise*3
    elif numero_gagnant%2 ==mise%2:
        mise = ceil(mise * 0.5)
        print("Vous êtes tomber sur la même couleur donc vous remportez", mise, "$.")
        argent += mise
    else:
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        argent -= mise

    if argent < 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False

    else:
        print("Vous avez à présent,", argent,"$")
        quitter = input("Souhaitez vous quitter le casino (y/n) :")
        if quitter == "y" or quitter == "Y":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False


