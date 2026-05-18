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
    lettres_du_mot=[]
    lettres_rentre=[]# une variable pour prendre les lettres suggeree en note et ne pas les suggerer dans lindice
    chance=6
    while chance>0:
        print ("mot : ",afficher(mot,lettres_du_mot),"le nombre de chance restant: ",chance)
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
        lettre_a_renter=input("entrez une lettre :")
        lettres_rentre.append(lettre_a_renter)
        if lettre_a_renter in mot:
            lettres_du_mot.append(lettre_a_renter)
        else:
            chance -= 1
        if "_" not in afficher(mot,lettres_du_mot):
            print("vous avez gagne , le mot est affectivement ",mot)
            return
    print("vous avez perdu, le mot est ",mot)

#la fonction pour commencer le jeu, et le choix de continuer ou pas
def boucle_de_jeu():
    while True:
        jouer()
        reponse=input("est ce que vous aimeriez rejouer ou non : repondez par oui ou non ")
        if reponse=="non":
            print("Merci !")
            break
        elif reponse!="oui":
            reponse=input("rentrez une reponse valide")

boucle_de_jeu()