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

#definir la fonction d'afficher l'etat du mot
def afficher(mot, lettres):
    resultat = ""
    i = 0
    while i < len(mot)+1:
        if mot[i] in lettres:
            resultat += mot[i] + " "
        else:
            resultat += "_ "
        i += 1

    return resultat
#definir la fonction du jeu
def Jouer():
    mot=mot_aleatoire()
    lettres_du_mot=[]
    chance=6
    while chance>0:
        print ("mot : ",afficher(mot,lettres_du_mot),"le nombre de chance restant: ",chance)
        if chance == 1:
            pas_dans_le_mot = []
            i = 0
            while i < len(mot):
                if mot[i] not in lettres_du_mot:
                    pas_dans_le_mot.append(mot[i])
                i += 1
            if len(pas_dans_le_mot) > 0:
                print("Indice :", random.choice(pas_dans_le_mot))
        lettre_a_renter=input("entrez une lettre :")
        if lettre_a_renter in mot:
            lettres_du_mot.append(lettre_a_renter)
        elif all(c in lettres_du_mot for c in mot):
            print("vous avez gagne")
        else:
            chance -= 1
            return
    print("vous avez perdu, le mot est ",mot)

