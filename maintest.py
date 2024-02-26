from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
import os, random, time, string, keyboard

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def WelcomeUsername():
    clear_console()
    print("Bien la venue dans cet univers virtuel merveilleuse\n")
    userName = input("selectionner votre nom d'utilisateur : ")
    while True:
        clear_console()
        L = False
        k = False
        if len(userName) < 3:
            L = True
            print('Erreur!')
            print("nom d'utilisateur trop court. Il doit etre de au moin 3 lettre")
            k = False
            for x in userName:
                if not x.isalpha():
                    print(f"'{x}' n'est pas une lettre, le nim d'utilisateur ne doit avoir que des lettres")
                    k = True
        else:
            k = False
            for x in userName:
                if not x.isalpha():
                    print(f"'{x}'n'est pas une lettre, le nom d'utilisateur ne doit avoir que des lettres")
                    k = True
        if L == False and k == False:
            clear_console()
            print(f"votre nom d'utilisateur est {userName}")
            break
        else:
            userName = input("Nom d'utilisateur : ")
    return userName

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
    printBonhomme(cbadtries)
    pass

def printBonhomme(badtries):
    if badtries==0:
        print("")
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      | ")
        print("=========")

    elif badtries==1:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |  ")
        print("=========")

    elif badtries ==2:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |  ")
        print("=========")

    elif badtries ==3:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |  ")
        print("=========")

    elif badtries ==4:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print("      |")
        print("      |  ")
        print("=========")

    elif badtries ==5:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" /    |")
        print("      |  ")
        print("=========")

    elif badtries ==6:
        print("")
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" / \\  |")
        print("      |  ")
        print("=========")

def choixMenu():
    print("Menu principal:\n", "1. Commencer une partie\n", "2. Afficher l'historique \n", "3. Quitter\n")
    print("choix : ", end="")
    choixM = input('')
    while choixM not in ["1", "2", "3"]:
        clear_console()
        print("Menu principal:\n", "1. Commencer une partie\n", "2. Afficher l'historique \n", "3. Quitter\n")
        print("Erreur : réponse doit etre, un nombre entier de 1 à 3, comme dans le menu")
        choixM = input('choix : ')
        clear_console()
    clear_console()
    return choixM
#----------------
def lectureHistorique(username):
    liste_historic=lire_historique_utilisateur(username)
    #print(liste_historic)
    print(f"Historique des parties de '{username}':\n")
    for x in liste_historic:
        resultHistoric= 'victoire' if x['resultat'] else 'defaite'
        print(f'date et heure : {x['timestamp']}; mot : {x['mot']}; resultat : {resultHistoric}; temps : {x['duree']} secondes\n')
    keyboard.wait('enter')
    trash = input()
    print(trash)
    clear_console()

def menuChoixDiff():
    clear_console()
    choixD=input("Choisir une difficulté:\n1. Facile\n2. Intermédiaire\n3. Difficile\n")
    while choixD not in ["1","2","3"]:
        clear_console()
        print(("Choisir une difficulté:\n1. Facile\n2. Intermédiaire\n3. Difficile\n"))
        print("Erreur : réponse doit etre, un nombre entier de 1 à 3, comme dans le menu")
        choixD=input("Entrer le nom de nouveau: ")
    return choixD

def wordGenerator(choixDiff):
    dic= lire_dictionnaires_mots()

    if choixDiff=="1":
            motList=dic["facile"]
            choosenWord=random.choice(motList)

    elif choixDiff=="2":
            motList=dic["intermediaire"]
            choosenWord=random.choice(motList)

    elif choixDiff=="3":
            motList=dic["difficile"]
            choosenWord=random.choice(motList)
        
    return choosenWord
    


def game():
    choixDiff=menuChoixDiff()
    wordGenerated = wordGenerator(choixDiff)
    ########################## intialize
    letterFound, letterRecord, positionnedLetter =[], [], [] # "positionnedLetter" variable is juste les lettres dans le mots
    for x in word: positionnedLetter.append(x)
    BadTries, GoodTries = 0, 0
    #party
    start_time = time.time()
    

    resultat = [start_time]]

    pass
    return resultat

def mainProcess():
    userName = WelcomeUsername()
    while True:
        choixM = choixMenu()
        if choixM == '1':

            resultGame = game()
            print(resultGame+'.')

            keyboard.wait('enter')
            trash = input()
            print(trash)
            clear_console()


            #enregistrer_partie(userName,generatedWord,resultGame[0],int(resultGame[2]))
            continue
            # The following variables are placeholders and need to be defined or implemented accordingly
            # choixDiff = ...
            # generatedWord = ...
            # resultOfGame = ...
            enregistrer_partie()
        elif choixM == '2':
            lectureHistorique(userName)
            continue
            # The following function call is a placeholder and needs to be defined or implemented accordingly
            # lectureDeLhistorique(userName)
            
            # The commented block below is an example of how to use keyboard events, adjust as needed
            """
            while True:
                if keyboard.is_pressed('enter'):
                    print('You pressed the "a" key!')
                    trash = input()
                    break
            """
            """

            liste_historic=lire_historique_utilisateur(userName)
            #print(liste_historic)
            print(f"Historique des parties de '{userName}':\n")
            for x in liste_historic:
                resultHistoric= 'victoire' if x['resultat'] else 'defaite'
                print(f'date et heure : {x['timestamp']}; mot : {x['mot']}; resultat : {resultHistoric}; temps : {x['duree']} secondes\n')
            
            """
        elif choixM == '3':
            print(3)
            break

# The code below appears to be commented out and includes placeholder or incomplete code.
# It's included as part of the script but will not execute unless uncommented and properly implemented.
"""
print(f"ended, username is {username}")

def entered_key():
    pass

while True:
    if keyboard.is_pressed():
        print('You pressed the "a" key!')
        trash = input()
        break
print("you went out")

a= input("1:")
b= input("2:")
print("a is :",a,"b is :",b)
"""
mainProcess()
clear_console()


