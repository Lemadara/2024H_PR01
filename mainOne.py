import os
from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
import random
import time
import string
import keyboard

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuNchoise():
	print("Menu principal:\n","1. Commencer une partie\n","2. Afficher l'historique \n","3. Quitter\n")

def diffMenu():
	diffValue=input("Choisir une difficulté:\n1. Facile\n2. Intermédiaire\n3. Difficile\n")
	return diffValue

def gameword(diff):
	exiter=0
	diC=lire_dictionnaires_mots()
	while True:

		if diff=="1":
			motList=diC["facile"]
			wordChoosen=random.choice(motList)

			exiter=1

		elif diff=="2":
			motList=diC["intermediaire"]
			wordChoosen=random.choice(motList)

			exiter=1

		elif diff=="3":
			motList=diC["difficile"]
			wordChoosen=random.choice(motList)
	    
			exiter=1

		else:
			while True:
				clear_console()
				print("Choisir une difficulté:\n1. Facile\n2. Intermédiaire\n3. Difficile\n")
				print("Erreur, entrée invalide, entrer un nombre de 1 à 3 de la selection de difficulté :",end='')

				diff=input(" ")
				if diff in ['1','2','3']:
					break
				else:
					...

		if exiter ==1:
			break
	return wordChoosen

def printOnwTries(wtries):


	if wtries==0:

		print("")
		print("  +---+")
		print("  |   |")
		print("      |")
		print("      |")
		print("      |")
		print("      | ")
		print("=========")
	elif wtries==1:

		print("")
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print("      |")
		print("      |")
		print("      |  ")
		print("=========")
	elif wtries ==2:

		print("")
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print("  |   |")
		print("      |")
		print("      |  ")
		print("=========")
	elif wtries ==3:

		print("")
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print(" /|   |")
		print("      |")
		print("      |  ")
		print("=========")
	elif wtries ==4:

		print("")
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print(" /|\\  |")
		print("      |")
		print("      |  ")
		print("=========")
	elif wtries ==5:

		print("")
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print(" /|\\  |")
		print(" /    |")
		print("      |  ")
		print("=========")
	elif wtries ==6:

		print("")
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print(" /|\\  |")
		print(" / \\  |")
		print("      |  ")
		print("=========")

def gameHeaderInfo(elWord,letterFound,wtries,letterRecord):
	clear_console()
	###print("admin info : word = ",elWord) # to retract # admin stuff

	#word visual - found letters and progression on finding the word
	print("mot : ",end="")

	for x in elWord:
		if x in letterFound:
			print(x,end=" ")
		else:
			print("_",end=" ")
	print("\nlettres trouvées : ",end='')
	for c in letterFound:
		print(c,end=" ")
	print('')
	print('lettres ratées: ',end='')
	for z in letterRecord:
		if z not in elWord:
			print(z,end=' ')

	# Le bonhomme pendu drawings progressing on numbers of wtries/number of wrong letters entered
	printOnwTries(wtries)
	pass

def game(elWord):
	# initial datas
	positionned=[]
	for x in elWord:
		positionned.append(x)
	print(positionned)
	letterFound=[]
	letterRecord=[]	
	wtries=0
	letterAlreadyEntered=False
	gtries=0
	
	#where the while begins
	while True:
		gameHeaderInfo(elWord,letterFound,wtries,letterRecord)
		"""clear_console()
								print("admin info : word = ",elWord) # to retract # admin stuff
						
								#word visual - found letters and progression on finding the word
								print("word : ",end="")
						
								for x in elWord:
									if x in letterFound:
										print(x,end=" ")
									else:
										print("_",end=" ")
						
								# Le bonhomme pendu drawings progressing on numbers of wtries/number of wrong letters entered
								printOnwTries(wtries)"""

		if letterAlreadyEntered:
			if letter in letterRecord:
				print("lettre deja entrée, réessayer: ",end='')
			#	print('\n',len(letterFound),len(positionned))
		elif not letterAlreadyEntered:
			print("essayer de deviner une lettre du mot: ",end='')
		#	print('\n',len(letterFound),len(positionned))

		letter=input("")

		if not(letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] or letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
			while True:
				gameHeaderInfo(elWord,letterFound,wtries,letterRecord)

				print("Error not a letter; \nTry again with a letter : ",end='')
				letter=input()
				if letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] or letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:

					break
		
		letter=letter.lower()

		# detect when a new letter is entered
		if letter not in letterRecord: # new letter
			letterRecord.append(letter)
			if letter in positionned: # in the word
				for x in positionned:
					if x ==letter:
						gtries+=1
				letterFound.append(letter)
			elif letter not in positionned: # not in the word
				wtries+=1

			letterAlreadyEntered=False

		elif letter in letterRecord:

			letterAlreadyEntered=True

		# we win or loose # when game ends
		if gtries==len(positionned):
			gameHeaderInfo(elWord,letterFound,wtries,letterRecord)
			return([True,wtries])
		elif wtries==7:
			return([False,wtries])

def welcome():
	while True:
		
		print("Entrer votre nom d'utilisateur:",end=' ')
		userName = input()
		clear_console()
		#splitedUName= list(userName)# not needed
		l=0

		if len(userName)>=3:
			print('')

		elif len(userName)<3:
			clear_console()
			print('Erreur: moin de 3 lettres\n')
			l=1

		for x in userName:
			if x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] or x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
				...
			else:
				print("char:",x)
				print(f"erreur : charactere '{x}' n'est pas une lettre")
				l=1

		if l==0:
			return userName
		
		print("\nVeuillez réessayer avec uniquement des lettres et au moins 3 lettres\n")

### code start program ########################################################################################################################################

# welcome and userName returned
userName=welcome()
print("votre nom d'utilisateur est: "+userName)	
input("..enter..")

# menu first apparition


#errorr=False # value to control when we go to menu level 1

# main events navigation
k=1
while True:
	while True:
		clear_console()
		menuNchoise()		
		choiseM=input("Choisi : ")
		
		while choiseM not in ['1','2','3']:
			clear_console()
			menuNchoise()	
			print("Erreur; entrer que un chiffre, 1, 2 ou 3 pour naviguer dans le menu")
			choiseM=input("Choisi : ")
		break

	if choiseM=='1':
		p=' '
		clear_console()
		choiDiff=diffMenu()

		#difficulties menu and choise - return choosen difficulty

		elWord=gameword(choiDiff)
		#generate El Word based on the difficulty choosen

		start_time = time.time()

		# game starts
		clear_console()
		result=game(elWord) # game result stored in result

		end_time = time.time()

		fTime = end_time-start_time
		iTime=int(fTime)

		if result[0]:
			print(f"Victoire : Félicitations '{userName}'! Vous avez deviné le mot '{elWord}' en {iTime} secondes et {result[1]} tentatives échouées.")
		elif not result[0]:
			print(f"Défaite : Dommage ! Le mot était {elWord}")

		print("Appuyez sur Entrée pour continuer vers le menu principal")
		#keyboard.wait('enter')
		#time.sleep(1)

		while True:
			keyboard.wait('enter')
			break
		k=0

		enregistrer_partie(userName,elWord,result[0],int(fTime))
		#errorr=False


		
	elif choiseM=='2':
		prr=' '

		# historic looking later
		clear_console()
		liste_historic=lire_historique_utilisateur(userName)
		#print(liste_historic)
		print(f"Historique des parties de '{userName}':\n")
		for x in liste_historic:
			resultHistoric= 'victoire' if x['resultat'] else 'defaite'
			print(f'date et heure : {x['timestamp']}; mot : {x['mot']}; resultat : {resultHistoric}; temps : {x['duree']} secondes\n')

		print("Appuyez Enter pour retourner")
		print('...Enter...',end='')
		while True:
			keyboard.wait('enter')
			break
		#errorr=False
		input('error false waiter')

		k=0

	elif choiseM=='3':
		clear_console()
		##quit program##
		print(f"merci d'avoir entrer le programme '{userName}', à une prochaine fois!")
		
		break
	
	"""else:
					while choiseM not in ['1','2','3']:
						clear_console()
						menuNchoise()
						print("error wrong number or a character or special character is entered")
						choiseM=input("please try again : ")
						k=1"""


# program ended
