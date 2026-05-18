import random
#definir la fonction qui enleve les accents
def enlever_accents(mot):
    accents ="àâäéèêëîïôöùûüç"
    sans_accents ="aaaeeeeiioouuuc"
    resultat = ""
    for c in mot:
        if c in accents:
            resultat += sans_accents[accents.index(c)]
        else:
            resultat += c
    return resultat
#definir la fonction d'Importation des mots
#le fichier doit etre enregistrer dans le dossier du projet.
def mot_aleatoire():
    with open("mots_pendu.txt") as fichier:
        mots = fichier.readlines()
    return enlever_accents(random.choice(mots).strip())

print(mot_aleatoire())