

from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
import os
import random
import time
import string
import keyboard

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Squelette du menu principal :
# Ce code peut être un bon point de départ.
# Il est possible de le modifier à votre guise ou de l'enlever complètement pour partir de zéro.

def WelcomeUsername():
    clear_console()

    print("Bien le venue chere joueur!\n")
    userName = input("donner votre nom d'utilisateur : ")
    while True:
        clear_console()
        v=0
        if len(userName)<3:
            v=1
            print('Erreur!')
            print("nom d'utilisateur trop court. Il doit etre de au moin 3 lettre")
            k=0
            for x in userName:
                if not (x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','É','È'] or x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','é','è']):
                    print(f"'{x}' n'est pas une lettre, le nim d'utilisateur ne doit avoir que des lettres")
                    k=1

        else:
            k=0
            for x in userName:
                if not (x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','É','È'] or x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','é','è']):
                    print(f"'{x}'n'est pas une lettre, le nom d'utilisateur ne doit avoir que des lettres")
                    k=1
        if v==0 and k==0:
            break
        else:
            userName=input("Nom d'utilisateur : ")

    return userName

def mainMenuChoise():
    clear_console()
    print("Menu principal:\n","1. Commencer une partie\n","2. Afficher l'historique \n","3. Quitter\n")
    print("choix : ",end="")
    choixMenuMain=input('')

    while choixMenuMain not in ["1","2","3"]:
        clear_console()
        print("Menu principal:\n","1. Commencer une partie\n","2. Afficher l'historique \n","3. Quitter\n")
        print("Erreur : réponse doit etre, un nombre entier de 1 à 3, comme dans le menu")
        choixMenuMain=input('choix : ')        

    return choixMenuMain

def ChoixDiffMenu():
    clear_console()
    choixDeDiff=input("Choisir une difficulté:\n1. Facile\n2. Intermédiaire\n3. Difficile\n")
    while choixDeDiff not in ["1","2","3"]:
        clear_console()
        print(("Choisir une difficulté:\n1. Facile\n2. Intermédiaire\n3. Difficile\n"))
        print("Erreur : réponse doit etre, un nombre entier de 1 à 3, comme dans le menu")
        choixDeDiff=input("Entrer le nom de nouveau: ")
    return choixDeDiff

def WordGenerator(choixDeDiff):
    dic= lire_dictionnaires_mots()

    if choixDeDiff=="1":
            motList=dic["facile"]
            wordChoosen=random.choice(motList)

    elif choixDeDiff=="2":
            motList=dic["intermediaire"]
            wordChoosen=random.choice(motList)

    elif choixDeDiff=="3":
            motList=dic["difficile"]
            wordChoosen=random.choice(motList)
        
    return wordChoosen

def gameinfo(word,letterFound,cbadtries,letterRecord):
    clear_console()
    # word letter évolution
    print("mot : ",end="")
    for x in word:
        if x in letterFound:
            print(x,end=" ")
        else:
            print("_",end=" ")

    # word letter found
    print("\nlettres trouvées : ",end='')
    for c in letterFound:
        print(c,end=" ")
    print('')

    # word letter mistakes
    print('lettres ratées: ',end='')
    for z in letterRecord:
        if z not in word:
            print(z,end=' ')

    # Le bonhomme pendu drawings progressing on numbers of cbadtries/number of wrong letters entered
    printBonhommeEvoluant(cbadtries)
    pass

def printBonhommeEvoluant(cbadtries):
    if cbadtries==0:
        print("")
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      | ")
        print("=========")

    elif cbadtries==1:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |  ")
        print("=========")

    elif cbadtries ==2:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |  ")
        print("=========")

    elif cbadtries ==3:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |  ")
        print("=========")

    elif cbadtries ==4:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print("      |")
        print("      |  ")
        print("=========")

    elif cbadtries ==5:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" /    |")
        print("      |  ")
        print("=========")

    elif cbadtries ==6:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" / \\  |")
        print("      |  ")
        print("=========")

def Game(word,userName):


    #initialisation
    letterFound, letterRecord, positionnedLetter =[], [], [] # "positionnedLetter" variable is juste les lettres dans le mots
    for x in word: positionnedLetter.append(x)
    countedBadTries, countedGoodTries = 0, 0

    #party
    start_time = time.time()
    while True:

        gameinfo(word, letterFound, countedBadTries, letterRecord)
        letterEnt=input("Entrer une lettre : ")
        while True:
            clear_console()

            if letterEnt not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'È','É']:
                gameinfo(word, letterFound, countedBadTries, letterRecord)
                print(f"Erreur: {letterEnt} n'est pas une lettre; Entrer que une seul lettre")
                letterEnt=input("Entrer une lettre : ")
            elif letterEnt in letterRecord:
                gameinfo(word, letterFound, countedBadTries, letterRecord)
                print(f"Erreur: {letterEnt} a deja été entré; Entrer une autre lettre individuel")
                letterEnt=input("Entrer une lettre : ")
            elif letterEnt not in letterRecord:
                letterRecord.append(letterEnt)
                if letterEnt in positionnedLetter:
                    letterFound.append(letterEnt)

                    countedGoodTries+=1
                else:
                    countedBadTries+=1
                break
            else:
                gameinfo(word, letterFound, countedBadTries, letterRecord)
                print(f"Erreur!? : La lettre {letterEnt} a deja été entrée, réessayer!")
                letterEnt=input("Entrer une lettre : ")              


        if countedGoodTries==len(word):
            end_time = time.time()
            timed=end_time - start_time

            clear_console()
            gameinfo(word, letterFound, countedBadTries, letterRecord)
            print(f"Victoire : Félicitations '{userName}'! Vous avez deviné le mot '{word}' en {int(timed)} secondes et {countedBadTries} tentatives échouées.")

            result=[True,countedBadTries,timed]
            return result
        elif countedBadTries==7:
            end_time = time.time()
            timed=end_time - start_time
            #gameinfo(word, letterFound, countedBadTries, letterRecord)

            clear_console()
            print(f"Défaite : Dommage ! Le mot était {word}")

            result=[False,countedBadTries,timed]
            return result
        pass
    pass


def mainProcess():
    userName=WelcomeUsername()
    print(f"Bienvenue {userName}!")
    time.sleep(2)

    while True:

        choix_menu_principal = mainMenuChoise()

        if choix_menu_principal == "1":
            # Demander à l'utilisateur de choisir une difficulté,
            choixDeDiff=ChoixDiffMenu()
            # sélectionner un mot aléatoire
            generatedWord=WordGenerator(choixDeDiff)
            # et commencer la partie.
            resultGame=Game(generatedWord,userName)

            enregistrer_partie(userName,generatedWord,resultGame[0],int(resultGame[2]))

            input("ENTRER pour retourner au menu principal")
            
            """print("Appuyer ENTRER pour quitter")
                                                keyboard.wait('enter')"""
            
            ...
        elif choix_menu_principal == "2":
            # Afficher l'historique de l'utilisateur.

            clear_console()
            liste_historic=lire_historique_utilisateur(userName)
            #print(liste_historic)
            print(f"Historique des parties de '{userName}':\n")
            for x in liste_historic:
                resultHistoric= 'victoire' if x['resultat'] else 'defaite'
                print(f'date et heure : {x['timestamp']}; mot : {x['mot']}; resultat : {resultHistoric}; temps : {x['duree']} secondes\n')
            
            """print("Appuyer ENTRER pour quitter")
                                                keyboard.wait('enter')
                                                print(' ')"""
            input("ENTRER pour retourner au menu principal")

        elif choix_menu_principal == "3":
            # Quitter le programme.
            clear_console()

            print(f"Hors le voir chere {userName}")
            break
            ...
        else:
            # Afficher un message d'entrée invalide.
            ...
clear_console()

mainProcess()


