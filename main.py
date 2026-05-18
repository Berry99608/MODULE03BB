import random

def mot_aleatoire():
    with open("mots_pendu.txt") as fichier:
        mots = fichier.readlines()
    return random.choice(mots).strip()

print("Mot sélectionné :", mot_aleatoire())