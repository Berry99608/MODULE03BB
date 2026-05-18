import random
#definir la fonction qui enleve les accents
def enlever_accents(mot):
    accents ="àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ"
    sans_accents="aaaeeeeiioouuucAAAEEEEIIOOUUUC"

    resultat = ""
    for c in mot:
        if c in accents:
            resultat += sans_accents[accents.index(c)]
        else:
            resultat += c
    return resultat
#definir la fonction d'Importation des mots
#le fichier doit etre enregistrer dans le dossier du projet.
# Fonction pour choisir un mot au hasard

def mot_aleatoire():
    with open("mots_pendu.txt") as f:
        return enlever_accents(random.choice(f.read().split()))
print(mot_aleatoire())