import os
from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
import random
import time
#import keyboard




def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuNchoise():
	clear_console()
	print("****MENU****\n"," 1 Commencer une partie\n"," 2 Afficher l'historique \n"," 3 Quitter\n","\n")

def diffMenu():
	diffValue=int(input("1 Facile\n2 Intermédiaire\n3 Difficile\n"))
	clear_console()
	return diffValue

def gameword(diff):
	exiter=0
	while True:

		if diff==1:
			diC=lire_dictionnaires_mots()
			motList=diC["facile"]
			wordChoosen=random.choice(motList)
	    
			print(wordChoosen)

			d=input('waiter')
			exiter=1

		elif diff==2:
			diC=lire_dictionnaires_mots()
			motList=diC["intermediaire"]
			wordChoosen=random.choice(motList)
	    
			print(wordChoosen)

			d=input('waiter')
			exiter=1

		elif diff==3:
			diC=lire_dictionnaires_mots()
			motList=diC["difficile"]
			wordChoosen=random.choice(motList)
	    
			print(wordChoosen)

			d=input('waiter')
			exiter=1

		else:
			print("Enter again or type 4 for exit")
			while True:
				diff=input(" : ")
				if diff==4:
					exiter=1
					break

		if exiter ==1:
			return wordChoosen



def game(elWord):
	tries=0
	listE=[]
	###
	start_time = time.time()

	multi=len(elWord)
	listW=elWord.split()

	###

	letter=input("give a letter")
	if letter not in listE and letter in listW:
		listE.append(letter)
		tries+=1

	if letter in listW:
		position=listW.index(letter)

	else:
		print("error try again with a real letter")

	while True:
		print(f"mots:"+"_"*multi)
		print(f"lettre trouvé:"+listW[position])
		print(f"")
		print(f"")
		print(f"")
		print(f"")
		print(f"")


	end_time = time.time()
	time = end_time-start_time
	print(time)
	return 0


clear_console()


### code start ########################################################################################################################################

# user name
print("give user name\n")
userName = input(" : ")
# menu first apparition

menuNchoise()
choiseM=int(input())
clear_console()

k=1 # value to control when we go to menu level 1

# main events navigation

while True:
	if k==0:

		menuNchoise()
		choiseM=int(input("Make a choice : "))
		clear_console()

	if choiseM==1:
		choiDiff=diffMenu()

		elWord=gameword(choiDiff)

		print(elWord)

		input("waiter")

		game(elWord)

		k=0
		
	elif choiseM==2:

		# historic looking later


		k=0
		
	elif choiseM==3:

		##FINISHED##
		
		break

	else:
		while choiseM not in [1,2,3]:
			
			menuNchoise()
			print("error wrong number or character")
			choiseM=int(input(" give it again : "))
			clear_console()
			k=1


	clear_console()	

print("exited")