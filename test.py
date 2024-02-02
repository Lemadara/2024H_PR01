import os
from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
import random
import time
print(" hello ")

#import keyboard

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
		print("admin info : word = ",elWord) # to retract # admin stuff

		#word visual - found letters and progression on finding the word
		print("word : ",end="")

		for x in elWord:
			if x in letterFound:
				print(x,end=" ")
			else:
				print("_",end=" ")

		# Le bonhomme pendu drawings progressing on numbers of wtries/number of wrong letters entered
		printOnwTries(wtries)

		if letterAlreadyEntered:
			if letter in letterRecord:
				print("letter already entered, try again : ",end='')
				print('\n'+len(letterFound)+len(positionned))
		elif not letterAlreadyEntered:
			print("try to guess a letter of the word : ",end='')
			print('\n'+len(letterFound)+len(positionned))


		letter=input("")

		if not(letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] or letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
			while True:
				print("Error not a letter; \nTry again with a letter : ",end='')
				letter=input()
				if letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] or letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
					break


		if letter not in positionned and letter not in letterRecord: # hmm wrong try if letter not in the word and if letter not in the record of entered letter
			wtries+=1
		if letter in positionned and letter not in letterRecord:
			gtries+=1
			
		# detect when a new letter is entered
		if letter not in letterRecord:
			letterRecord.append(letter)
			if letter in positionned:
				letterFound.append(letter)
			letterAlreadyEntered=False

		elif letter in letterRecord:
			letterAlreadyEntered=True

		# we win or loose # when game ends
		if gtries==len(positionned):
			return(["won",wtries])
		elif wtries==7:
			return(["lost",wtries])
#	return 0

def welcome():
	while True:
		print("Entrer votre nom d'utilisateur:",end=' ')
		userName = input()
		#splitedUName= list(userName)# not needed
		l=0

		if len(userName)>3:
			print('')
		elif len(userName)<3:

			print('error: less than 3 letters\n')
			l=1

		for x in userName:
			if x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] or x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
				...
			else:
				print("char:",x)
				print(f"error : uncorrect {x} not a letter")
				l=1

		if l==0:
			return userName
		
		print("\nplease try again with only letters and at least 3 letters\n")
def gameword(diff):
	exiter=0
	diC=lire_dictionnaires_mots()
	while True:

		if diff=="1":
			motList=diC["facile"]
			wordChoosen=random.choice(motList)
			print(wordChoosen)

			d=input('waiter1 word')
			exiter=1

		elif diff=="2":
			motList=diC["intermediaire"]
			wordChoosen=random.choice(motList)
	    
			print(wordChoosen)

			d=input('waiter1.2 word ')
			exiter=1

		elif diff=="3":
			motList=diC["difficile"]
			wordChoosen=random.choice(motList)
	    
			print(wordChoosen)

			d=input('waiter1.3 word ')
			exiter=1

		else:
			while True:
				print("Erreur, entrée invalide, entrer un nombre de 1 à 3 de la selection :")

				diff=input(" : ")
				if diff in ['1','2','3']:
					break
				else:
					...

		if exiter ==1:
			break
	return wordChoosen
#====
elWord=gameword(1)

userName=welcome()
print("your username is : "+userName)	
input("waiter #dev")

#	start time, start game
start_time = time.time()
input('waiter for time')
result=[True,12]

print("\nResult : ",result)

end_time = time.time()

ftime = end_time-start_time
print("\n",ftime)

print((userName,elWord,result[0],int(ftime)))
print(type(userName),type(elWord),type(result[0]),type(int(ftime)))


