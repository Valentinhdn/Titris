from datetime import datetime
import random
from os import system, name



############################# BLOCS #############################

# ===================================
# TOUS BLOCS DE TOUS LES PLATEAUX
l1 = [[1,0],[1,1]]
l2 = [[0,1],[1,1]]
l3 = [[1,1],[0,1]]
l4 = [[1,1],[1,0]]
h = [[1,1],[1,1]]

L1 = [[1,1],[0,1],[0,1]]
L2 = [[1,0],[1,0],[1,1]]
K1 = [[1,0],[1,1],[1,0]]
K2 = [[0,1],[1,1],[0,1]]
Y1 = [[1,0],[1,1],[0,1]]
Y2 = [[0,1],[1,1],[1,0]]

j1 = [[0,1,0],[1,1,1]]
j2 =[[1,1,1],[0,1,0]]
z1 = [[1,1,0],[0,1,1]]
z2 = [[0,1,1],[1,1,0]]
a1 = [[1,0,0],[1,1,1]]
a2 = [[0,0,1],[1,1,1]]

I1 = [[1,1,1,1]]
o = [[1]]

I2 = [[1],[1],[1],[1]]

# ===================================
# TOUS BLOCS DU PLATEAU CERCLE
II2 = [[1,1,1,1],[1,1,1,1]]
ch = [[1,1,1,1],[1,1,1,0]]  

O = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
Ω = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[0,1,1,0]]
U = [[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]
Linv = [[1,1,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
Uinv = [[1,1,1],[0,0,1],[0,0,1],[1,1,1]]
II1 = [[1,1],[1,1],[1,1],[1,1]]
M = [[1,1,1,1,1],[1,0,0,0,1],[0,0,0,0,0],[1,1,1,1,1]]
J = [[1,0,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

i5 = [[1],[1],[1],[1],[1]]

# ===================================
# TOUS BLOCS DU PLATEAU LOSANGE
i5penché = [[1,1,1,1,1]]

lpenché = [[1,1,1,1],[0,0,0,1]]

v = [[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
Tpenché = [[0,0,0,1],[1,1,1,1],[0,0,0,1]]

q1 = [[0,0,1,1],[0,1,1,0],[1,1,0,0],[1,0,0,0]]
q2 = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]]
q3 = [[1,0,0,0],[1,1,0,0],[0,1,1,0],[0,0,1,1]]
q4 = [[0,0,0,1],[0,0,1,1],[0,1,1,0],[1,1,0,0]]
T = [[1,1,1,1],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
X = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]
l = [[1,0],[1,0],[1,0],[1,1]]
linv = [[1,1],[0,1],[0,1],[0,1]]
O = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

i5 = [[1],[1],[1],[1],[1]]

# ===================================
# TOUS BLOCS DU PLATEAU TRIANGLE
i3penché = [[1,1,1]]
i2penché = [[1,1]]

i2 = [[1],[1]]

Z = [[1,0,0],[1,1,1],[0,0,1]]
Z90 = [[1,1,0],[0,1,0],[0,1,1]]
Z180 = [[0,0,1],[1,1,1],[1,0,0]]
Z360 = [[0,1,1],[0,1,0],[1,1,0]]
diagonal1 = [[0,0,1],[0,1,0],[1,0,0]]
diagonal2 = [[1,0,0],[0,1,0],[0,0,1]]
i3 = [[1],[1],[1]]
plus = [[0,1,0],[1,1,1],[0,1,0]]



############################# LISTE DES BLOCS #############################

# ===================================
# BLOCS COMMUNS À TOUS LES PLATEAUX
liste_commun = [l1, l2, l3, l4, h, L1, L2, K1, K2, Y1, Y2, j1, j2, z1, z2, a1, a2, I1, I2, o]
# print(un_pour_tous(liste_commun))

# ===================================
# BLOCS PROPRE AU PLATEAU LOSANGE
liste_losange = [i5penché, lpenché, v, Tpenché, q1, q2, q3, q4, T, X, l, linv, O, i5]
# print(un_pour_tous(liste_losange))

# ===================================
# BLOCS PROPRE AU PLATEAU TRIANGLE
liste_triangle = [i3penché, i2penché, i2, Z, Z90, Z180, Z360, diagonal1, diagonal2, i3, plus]
# print(un_pour_tous(liste_triangle))

# ===================================
# BLOCS PROPRE AU PLATEAU CERCLE
liste_cercle = [II2, ch, O, Ω, U, Linv, Uinv, II1, M, J, i5]



# Idée de créer un tableau des scores pour facile et difficile (liste de dictionnaires trié via un quicksort --> avc PRENOM DATE SCORE) qui s'ajoute à la fin d'une partie
scoreboard = [ {'Pseudo': 'Hamilton' , 'Score' : 0 , 'Date' : '2023-01-01', 'Heure': '08:37', 'Mode': 'FACILE', 'Grille': 'LOSANGE'},
            {'Pseudo': 'Roger Federer' , 'Score' : 1200, 'Date' : '2022-12-17', 'Heure': '18:42', 'Mode': 'FACILE' , 'Grille': 'CERCLE'},
            {'Pseudo': 'Halim_bot(0)' , 'Score' : 134, 'Date' : '2023-01-20', 'Heure': '10:00', 'Mode': 'FACILE' , 'Grille': 'CERCLE'},
            {'Pseudo': 'V' , 'Score' : 450, 'Date' : '2077-11-24', 'Heure': '23:59', 'Mode': 'DIFFICILE' , 'Grille': 'LOSANGE'} ]
            


############################# FONCTION CLEAR #############################


def clear():
    if name == 'nt': # pour windows
        _ = system('cls')
    else: # pour mac et linux
        _ = system('clear')

clear()

############################# AFFICHAGE DE LA GRILLE #############################

def read_plateau(file):

    grille = []
    doc = open(file, "r")
    donnees = doc.readlines()

    for line in donnees:
        li = []
        for element in line:
            if element == "1":
                li.append(1)
            if element == "2":
                li.append(2)
            if element == "0":
                li.append(0)
        grille.append(li)
    
    return grille

alphabet= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']





def affichage_plateau(grid):
    print(' ')
    print('    a b c d e f g h i j k l m n o p q r s')
    print('    _____________________________________')

    alpha_ind = 0
    for line in grid:
        print(f"{alphabet[alpha_ind]} ǁ " , end="")
        for el in line:
            if el == 1:
                print(". ", end= "")
            if el == 2:
                print("▣ ", end= "")
            if el == 0:
                print("  ", end= "")
        print(' ǁ', end="") 
        print()
        alpha_ind += 1
    print('    _____________________________________')
    print('    a b c d e f g h i j k l m n o p q r s \n')
    



grille_losange = read_plateau("losange.txt")
grille_triangle = read_plateau("triangle.txt")
grille_cercle = read_plateau("cercle.txt")



############################# AFFICHAGE DES BLOCS #############################

def blocs_MxN(liste2D): # Fonctionne pour toutes les matrices en faisant automatiquement l'ajustement du nombre de ligne
    n = 0
    #while n != len(liste2D) :
    for n in range(len(liste2D)) :
        print(f'\nBloc {n + 1}:')
        for element in liste2D[n]: # Pour lire la matrice ligne par ligne 
            for ind in element : # Consulte les éléments 1 par 1 ligne par ligne   
                if ind == 1 :
                    print('▩', end =" ")
                else:
                    print('.', end =" ") 
            print() # Pour revenir à la ligne et traduire la ligne suivante
        n += 1 

    return '' # Pour pas avoir de None qui s'affiche à la fin du block



def blocs_MxN_jeu(bloc, pos): # Fonctionne pour toutes les matrices en faisant automatiquement l'ajustement du nombre de ligne
    
    print(f'\nBloc {pos}:')
    for element in bloc: # Pour lire la matrice ligne par ligne 
        for ind in element : # Consulte les éléments 1 par 1 ligne par ligne   
            if ind == 1 :
                print('▩', end =" ")
            else:
                print('.', end =" ") 
        print() # Pour revenir à la ligne et traduire la ligne suivante

    return '' # Pour pas avoir de None qui s'affiche à la fin du block



def affichage_blocs(regle, types, liste_bloc, score):

    if types == 'LOSANGE':
        list_select = liste_commun + liste_losange        
    elif types == 'CERCLE':
        list_select = liste_commun + liste_cercle
    elif types == 'TRIANGLE':
        list_select = liste_commun + liste_triangle

    if regle == 'FACILE':
        for bloc in list_select:
            liste_bloc.append(bloc)
    elif regle == 'DIFFICILE':
        
        if score > 100: #Pour proposer des blocs plus gros à mesure que le score augmente
            select_bloc_modifié = []
            for i in list_select:
                compt = val_bloc([i]) 
                if compt >= 4 :
                    select_bloc_modifié.append(i)
            list_select = select_bloc_modifié

        if score > 200 and types == 'LOSANGE' or types == 'CERCLE': #Pour proposer des blocs plus gros à mesure que le score augmente
            select_bloc_modifié = []
            for i in list_select:
                compt = val_bloc([i]) 
                if compt >= 6 :
                    select_bloc_modifié.append(i)
            list_select = select_bloc_modifié

        if score > 300 and types == 'LOSANGE' or types == 'CERCLE' : #Pour proposer des blocs plus gros à mesure que le score augmente
            select_bloc_modifié = []
            for i in list_select:
                compt = val_bloc([i]) 
                if compt >= 7:
                    select_bloc_modifié.append(i)
            list_select = select_bloc_modifié

        for i in range(3):
            cond = False
            while cond == False: #Pour éviter d'avoir les mêmes blocs proposés aléatoirement
                aleatoire = random.choice(list_select)
                if aleatoire not in liste_bloc:
                    cond = True
            liste_bloc.append(aleatoire)


    elif regle == 'GUIDED':
        if types == 'LOSANGE':
            choix_grille = grille_losange
        if types == 'TRIANGLE':
            choix_grille = grille_triangle
        if types == 'CERCLE':
            choix_grille = grille_cercle
        

        for bloc in list_select:
            test = dispo_placement_bis(choix_grille,bloc)
            if test == True:
                liste_bloc.append(bloc)
        
    return ''


# QUICKSORT 

def partitionate(tab, f, l, p):
    max =l
    while f < l:
        while tab[f] <= tab[p] and f < max:
            f += 1
        while tab[l] >= tab[p] and l > p :
            l -= 1
        if f<l:
            tab[f], tab[l] = tab[l], tab[f]
        tab[p], tab[l] = tab[l], tab[p]
    return l

def quicksort(tab, f, l):
    if(f>l):
        return
    p = partitionate(tab, f, l, f)
    quicksort(tab,f, p-1)
    quicksort(tab,p+1, l)

############################# TENTATIVE ET PLACEMENT DE BLOC #############################


# Placer un bloc

dict_Y = { 'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S':18 }
dict_X = { 'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17 ,'s':18 }

choix_grille = grille_losange


def test_placement(types,bloc, pos):
    val = True
    affichage_plateau(choix_grille)
    blocs_MxN_jeu(bloc, pos)   

    print("\n Selectionner des coordonnées correspondant au point en bas à gauche de la figure à placer\n")

    try:
        coord_y = dict_Y[input("Quelle coordonnée en ordonnée avez-vous choisi ? \nTapez une lettre en MAJUSUCULE : ").upper()]
        coord_x = dict_X[input("Quelle coordonnée en abcisse avez-vous choisi ? \nTapez une lettre en MINUSCULE : ").lower()]
    except KeyError:
        print("\n ATTENTION, vos entrées sont erronées! Vous n'aurez pas d'autres avertissements \n")

        coord_y = dict_Y[input("Quelle coordonnée en ordonnée avez-vous choisi ? \nTapez une lettre en MAJUSUCULE : ").upper()]
        coord_x = dict_X[input("Quelle coordonnée en abcisse avez-vous choisi ? \nTapez une lettre en MINUSCULE : ").lower()]

    for line in range(1,len(bloc)+1):
        for el in range(len(bloc[0])):
            try:
                if types[coord_y - line+1][coord_x + el] !=1 :
                    if bloc [-line][el] == 1:
                        val = False
                        break
            except IndexError:
                val = False
                break
    if val == False:
        #print(affichage_plateau(types))
        return val
    else:
        for line in range(1,len(bloc)+1):
            for el in range(len(bloc[0])):
                types[coord_y - line+1][coord_x + el] += bloc [-line][el]
        #print(affichage_plateau(types))
        return val


############################# FONCTIONNALITÉ AVANCÉE #############################

def dispo_placement_bis(grille,bloc):
    val = False


    key_x = list(dict_X.keys())
    key_y = list(dict_Y.keys())

    verif = []
    for x in key_x:
        for y in key_y:

            val_verif = True
            coord_x = dict_X[x.lower()]
            coord_y = dict_Y[y.upper()]
            for line in range(1,len(bloc)+1):
                for el in range(len(bloc[0])):
                    try:
                        if grille[coord_y - line+1][coord_x + el] !=1 :
                            if bloc [-line][el] == 1:
                                val_verif = False
                            break
                    except IndexError:
                        val_verif = False
                        break
            verif.append(val_verif)         
    
    for i in verif:
        if i == True:
            val = True

    return val

############################# CHUTE DE BLOC ET SUPPRESSION LIGNES/COLONNES #############################
        


def chute_blocs(grille,borne, regle):
    if regle == 'DIFFICILE' or regle =='GUIDED':
        for ligne in range(borne):
            for el in range(len(grille[ligne])):
                if grille[borne-ligne][el] == 1:
                    if grille[borne-ligne-1][el] == 2:
                        grille[borne-ligne][el], grille[borne-ligne-1][el]  = grille[borne-ligne-1][el],grille[borne-ligne][el]

    if regle == 'FACILE':
        for i in range(len(grille)):
            for ligne in range(len(grille)):
                for el in range(len(grille[ligne])):
                    if grille[borne-ligne][el] == 1:
                        if grille[borne-ligne-1][el] == 2:
                            grille[borne-ligne][el], grille[borne-ligne-1][el]  = grille[borne-ligne-1][el],grille[borne-ligne][el]



def suppression_ligne(grille,ligne, regle):
    
    for posi in range(len(grille[ligne])):
        if grille[ligne][posi] != 0:
            grille[ligne][posi] = 1
    
    chute_blocs(grille,ligne,regle)
    
    

def suppression_colonne(grille,colonne):
    for rang in range(len(grille)):
        if grille[rang][colonne] != 0:
            grille[rang][colonne] = 1
    


def clear_grille(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] != 0:
                grille[i][j] = 1



def test_lignes(grille,types):
    points = 0
    lignes_a_supprimer = []

    if types == 'CERCLE':
        for ligne in range(len(grille)): #faire démarrer à 1 si besoin
            val = True # On assume que la ligne va se supprimer car la ligne serait complète
            count = 0
            for el in range(len(grille[ligne])):
                if grille[ligne][el] != 0:
                    count += 1
                    if grille[ligne][el] == 1: # Si une case n'est pas remplie, 
                        val = False # alors la ligne ne sera pas complète
                    
            if val == True:
                points += count
                lignes_a_supprimer.append(ligne)

        return points, lignes_a_supprimer
    
    elif types =='LOSANGE':
        for ligne in range(1,len(grille)-1): 
            val = True # On assume que la ligne va se supprimer car la ligne serait complète
            count = 0
            for el in range(len(grille[ligne])):
                if grille[ligne][el] != 0:
                    count += 1
                    if grille[ligne][el] == 1: # Si une case n'est pas remplie, 
                        val = False # alors la ligne ne sera pas complète
                    
            if val == True:
                points += count
                lignes_a_supprimer.append(ligne)

        return points, lignes_a_supprimer

    else:
        for ligne in range(1,len(grille)): 
            val = True # On assume que la ligne va se supprimer car la ligne serait complète
            count = 0
            for el in range(len(grille[ligne])):
                if grille[ligne][el] != 0:
                    count += 1
                    if grille[ligne][el] == 1: # Si une case n'est pas remplie, 
                        val = False # alors la ligne ne sera pas complète
                    
            if val == True:
                points += count
                lignes_a_supprimer.append(ligne)
        return points, lignes_a_supprimer



def test_colonnes(grille,types):
    points = 0
    colonnes_a_supprimer = []

    if types == 'CERCLE':
        for rang in range(len(grille[0])):
            val = True # On assume que la ligne va se supprimer car la ligne serait complète
            count = 0
            for posi in range(len(grille)): 
                if grille[posi][rang] != 0:
                    count += 1
                    if grille[posi][rang] == 1: # Si une case n'est pas remplie, 
                        val = False # alors la ligne ne sera pas complète
                    
            if val == True:
                points += count
                colonnes_a_supprimer.append(rang)

        return points, colonnes_a_supprimer

    elif types == 'LOSANGE':
        for rang in range(1,len(grille[0])-1):
            val = True # On assume que la ligne va se supprimer car la ligne serait complète
            count = 0
            for posi in range(len(grille)): 
                if grille[posi][rang] != 0: 
                    count += 1
                    if grille[posi][rang] == 1: # Si une case n'est pas remplie, 
                        val = False # alors la ligne ne sera pas complète
                    
            if val == True:
                points += count
                colonnes_a_supprimer.append(rang)

        return points, colonnes_a_supprimer
    
    else:
        for rang in range(1,len(grille[0])-1):
            val = True # On assume que la ligne va se supprimer car la ligne serait complète
            count = 0
            for posi in range(len(grille)): 
                if grille[posi][rang] != 0: 
                    count += 1
                    if grille[posi][rang] == 1: # Si une case n'est pas remplie, 
                        val = False # alors la ligne ne sera pas complète
                    
            if val == True:
                points += count
                colonnes_a_supprimer.append(rang)

        return points, colonnes_a_supprimer

############################# AUTRE FONCTIONNALITÉ AVANCÉE #############################

def val_bloc(liste2D): # fonction pour vérifier la valeur de chaque bloc (son nombre de ▩)
    n = 0
    cmpt = 0
    while n != len(liste2D) :
        for element in liste2D[n]: # Pour lire la matrice ligne par ligne 
            for ind in element : # Consulte les éléments 1 par 1 ligne par ligne   
                if ind == 1 :
                    cmpt += 1 # compter le nombre de ▩
        n += 1 
    return cmpt
            

############################# REGLAGES PAR DÉFAUT #############################

# Pour lancer le jeu sans paramétrer manuellement :
regle = 'FACILE' # Règle par défaut
types = 'TRIANGLE' # Type par défaut
choix_grille  = grille_triangle # Grille par défaut








############################# MENU #############################

menu = 0

while menu >= 0 and menu < 5:

    print()
    print("______________________________________________")
    print("Bienvenue sur notre Titris multidimensionnel !")
    print("______________________________________________\n")
      
    print("1) Connaitre les règles du jeu \n")
    print("2) Paramètres du jeu \n")
    print("3) Commencez à jouer ! \n")
    print("4) Tableau des scores \n")
    print("5) Quitter \n")

    menu = int(input("Que souhaitez-vous effectuer ? Saisissez un numéro : ")) 




    if menu == 1:
        clear()
        print('\n\n\n',"                                  RÈGLE DU JEU")
        print("                                   ============",'\n')
        print("Si vous commencez à jouer sans configurer les paramètres du jeu, le jeu sera par défaut sur un plateau TRIANGLE en mode FACILE.\n")
        print("Vous pouvez modifier ces paramètres dans 'Paramètres du jeu' !") 
        print("Ceci vous permet d'accéder à d'autres plateaux de jeu et de régler la difficulté sur GUIDED, FACILE ou DIFFICILE.\n")
        print("Le mode GUIDED ne propose que les blocs qui peuvent rentrer dans la grille.")
        print("Le mode FACILE popose tous les blocs disponibles pour le plateau")
        print("Le mode DIFFICILE propose uniquement 3 blocs aléatoires\n")
        print("Tous les plateaux de jeu contiennent les blocs communs mais ont chacun leurs blocs de jeu spécifiques en plus !")
        print("Durant la session de jeu, il est nécessaire d'insérer les coordonnées en bas à gauche de la forme pour placer le bloc sur le plateau.\n")
        print("Vous gagnez quelques points lorsque vous posez un bloc et encore plus de points lorsque vous supprimez une ligne ou une colonne.")
        print("Pour supprimer une ligne ou une colonne, il vous suffit de la compléter entièrement avec les blocs proposés.",'\n')
        print("Il est important de notifier que la chute des blocs est différente selon la difficulté :")
        print("-En mode FACILE, les blocs tomberont le plus bas possible dès qu'une ligne est complétée,")
        print("-En mode DIFFICILE, les blocs ne tomberont que d'une seule ligne\n")
        print("Attention !! Si vous vous trompez trop de fois de suite sur le placement des blocs, vous perdrez la partie !!.\n\n")
        print("                               Amusez-vous bien :) !\n\n\n")




    if menu == 2:

        ############################# PARAMETRAGE DE JEU #############################

        clear()
        types = 0
        while types != 'QUIT':

            print("\nCommençons d'abord par choisir la dimension du plateau de jeu, tapez :\n" )
            
            print("LOSANGE pour avoir un plateau en forme de losange ")
            print("TRIANGLE pour avoir un plateau en forme de triangle ")
            print("CERCLE pour avoir un plateau en forme de cercle ")
            
            types = input("\nQu'avez-vous choisi ? \n").upper()

            if types == 'LOSANGE':
                affichage_plateau(grille_losange)
                choix_grille  = grille_losange

            if types == 'TRIANGLE':
                affichage_plateau(grille_triangle)
                choix_grille  = grille_triangle

            if types == 'CERCLE':
                affichage_plateau(grille_cercle)
                choix_grille  = grille_cercle
          
            print("\nVoulez-vous confirmer votre sélection ?")
            choix= input("OUI ou NON: ").upper()
            if choix == 'OUI':
                break
        
               
        regle = 0

        while regle != 'QUIT':
            print("\nVeuillez désormais sélectionner comment les blocs seront suggérés \n" )

            print("Mode FACILE : Affiche l'ensemble des blocs disponibles")
            print("Mode DIFFICILE : Sélectionne aléatoire 3 blocs")
            print("Mode GUIDED : Propose uniquement les blocs pouvant être posés sur le plateau")

            regle = input("\nQuel mode avez-vous choisi pour lancer le jeu ? ").upper()
        
            print(f"\nVous avez décidé de paramétrer le jeu en mode {regle.lower()} sur un tableau en forme de {types.lower()}")
            choixx= input("Voulez-vous confirmer votre sélection ? \nOUI ou NON: ").upper()
            if choixx == 'OUI':
                break




    if menu == 3 :

        ############################# BOUCLE DE JEU #############################

        clear()
        print(f"\nType : {types}\nDifficulté: {regle}")

        print("\nBonne partie !\n")


        erreur = 0
        names = input("Quel est votre pseudo ? : ")
        score = 0
        while erreur <4:
            clear()

            

            # Si on peut toujours jouer, alors on peut placer un bloc
            affichage_plateau(choix_grille)    
            print("                  ===========")        
            print(f"                  SCORE : {score}")
            print("                  ===========",'\n')   
            select_bloc = []
            affichage_blocs(regle, types, select_bloc, score)            
            blocs_MxN(select_bloc)

            if (len(select_bloc)) >= 10: #Pour afficher la grille à nouveau si la liste de blocs disponibles est trop grande
                    affichage_plateau(choix_grille) 
                    print("                  ===========")
                    print(f"                  SCORE : {score}")
                    print("                  ===========",'\n') 


            

            ############################# VERIF ERREUR / SORTIE POSSIBLE #############################
            if erreur == 1:
                print (f"\nImpossible de poser le bloc ! Veuillez réessayer ! \n\nIl vous reste {3-erreur} tentatives")
                print("             ---\n")

            if erreur ==2:
                print("OULALAAAAAA ! Il ne vous reste QU'UNE SEULE tentative ! Soyez malins \n")
            if erreur ==3:
                print("PERDUUUUUUU !!!!")
                val = False
                for i in range(len(scoreboard)):
                    if scoreboard[i]['Pseudo'] == names: # Comparaison entre le pseudo du joueur et ceux dans scoreboard
                        if scoreboard[i]['Mode'] != types:
                            if scoreboard[i]['Score'] <= score:
                                val = True
                                arg = i
                        
                if val == True:
                    scoreboard[arg]['Score'] = score
                    scoreboard[arg]['Date'] = (str(datetime.today())).split()[0]
                else:    
                    scoreboard.append(  {'Pseudo':names, 'Score': score, "Date": (str(datetime.today())).split()[0], 'Heure': (str(datetime.today())).split()[1][:5], 'Mode': regle, 'Grille': types}) 
                clear_grille(choix_grille)
                break


            ############################# TENTATIVE ET PLACEMENT DE BLOC #############################
            try:
                vari = int(input("\nQuel bloc souhaitez-vous placer ? Indiquez le numéro du Bloc "))
                clear()
            except ValueError:
                print("\nVérifiez bien l'index choisi! ")
                vari = int(input("\nQuel bloc souhaitez-vous placer ? Indiquez le numéro du Bloc ")) 
                clear()

            tentative = test_placement(choix_grille,select_bloc[vari-1], vari)

            if tentative == True:

                repet = max(len(choix_grille),len(choix_grille[0]))
                for i in range(repet):
                    points_ligne , liste_lignes = test_lignes(choix_grille,types)
                    points_colonne , liste_colonnes = test_colonnes(choix_grille,types)

                    for col in liste_colonnes:
                        suppression_colonne(choix_grille,col)
                    for li in liste_lignes:
                        suppression_ligne(choix_grille,li, regle)

                if points_ligne > 1 and points_colonne > 1:
                    score +=  points_ligne * 2 * points_colonne + 50
                    print("Bravo ! Vous avez réalisé un combo ! \n")
                else:
                    score +=  points_ligne * 2 + points_colonne + 2 * val_bloc([select_bloc[vari-1]])
                erreur = 0
            
            else: 
                erreur += 1
            
            
            

    if menu == 4:
        clear()
        order = []
        for i in range(len(scoreboard)):
            order.append(scoreboard[i]['Score'])
        quicksort(order,0, len(order)-1)    # Afin d'ordonner notre liste de score et pour les afficher de façon décroissante
        order_inv = order[::-1]
        
        print("\n\n                       PODIUM !!!")
        print("                       ----------")
        for j in range(len(scoreboard)):           
            for k in range(len(scoreboard)):
                if scoreboard[k]['Score'] == order_inv[j]:
                    print("\n===================", '\n')
                    print((f"Score de {scoreboard[k]['Score']} points\nRéalisé par {scoreboard[k]['Pseudo']} \nLe {scoreboard[k]['Date']} à {scoreboard[k]['Heure']}\nEn mode {scoreboard[k]['Mode']} sur un plateau {scoreboard[k]['Grille']}"))
            
            if j ==2:
                print("\n\n                       LES AUTRES...")
                print("                       -------------")

