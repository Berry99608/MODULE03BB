import random
#definir la fonction qui enleve les accents
def enlever_accents(mot):
    accents ="àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ"
    sans_accents="aaaeeeeiioouuucAAAEEEEIIOOUUUC"
    resultat = ""
    for d in mot:
        if d in accents:
            resultat += sans_accents[accents.index(d)]
        else:
            resultat += d
    return resultat
#definir la fonction d'Importation des mots

#le fichier doit etre enregistrer dans le dossier du projet.

# Fonction pour choisir un mot au hasard

def mot_aleatoire():
    with open("mots_pendu.txt") as f:
        return enlever_accents(random.choice(f.read().split()))

#definir la fonction d'afficher l'etat du mot
def afficher(mot, lettres_du_mot):
    resultat = ""
    i = 0
    while i < len(mot):
        if mot[i] in lettres_du_mot:
            resultat += mot[i] + " "
        else:
            resultat += "_ "
        i += 1

    return resultat
#definir la fonction du jeu
def jouer():
    mot=enlever_accents(mot_aleatoire())
    lettres_du_mot=[] # lettres correctes
    lettres_rentre=[]# une variable pour prendre les lettres suggerees en note et ne pas les suggerer dans l'indice
    chance=6
    while chance>0:
        print (" le mot : ",afficher(mot,lettres_du_mot),"le nombre de chance: ",chance)
        # Indice (dernière chance)
        if chance == 1:
            pas_dans_le_mot = []
            alphabet="abcdefghijklmnopqrstuvwxyz"
            i = 0
            while i < len(alphabet):
                if alphabet[i] not in lettres_rentre:
                    pas_dans_le_mot.append(alphabet[i])
                i += 1
            if len(pas_dans_le_mot) > 0:
                print("Indice : une lettre qui n'est pas dans le mot :", random.choice(pas_dans_le_mot))
        # Entrée utilisateur
        lettre_a_renter=input("Entrez une lettre :")
        lettres_rentre.append(lettre_a_renter)
        if lettre_a_renter in mot:
            lettres_du_mot.append(lettre_a_renter)
            print("la lettre:",lettre_a_renter,"est dans le mot.")
        else:
            chance -= 1
        # Condition de victoire
        if "_" not in afficher(mot,lettres_du_mot):
            print("Bravo ! Vous avez gagne , le mot est effectivement ",mot)
            return
    # Défaite
    print("Vous avez perdu! le mot est ",mot)

#la fonction pour commencer le jeu, et le choix de continuer ou pas
def boucle_de_jeu():
    print("Bienvenue au jeu du pendu :")
    print("La machine choisira un mot aleatoire de la liste fournie , et vous devez le deviner.")
    while True:
        jouer()
        reponse=input("Est ce que vous aimeriez rejouer ou non : repondez par oui ou non ")
        if reponse=="non":
            print("Merci d'avoir joué !")
            break
        elif reponse!="oui":
            reponse=input("rentrez une reponse valide")

boucle_de_jeu()