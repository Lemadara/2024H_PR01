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
	###	Game starts
	# initial datas
	position={}	
	positionned=[]
	for x in elWord:
		if x not in positionned:
			position[x]=[]
			positionned.append(x)
	letterFound=[]
	letterRecord=[]

	tries=0
	wtries=0


	#where the while begins
	while True:

		print("admin info : word = ",elWord) # to retract # admin stuff

		print("word : ",end="")
		### where to implant it
		for x in elWord:
			if x in letterFound:
				print(x,end=" ")
			else:
				print("_",end=" ")

		printOnwTries(wtries)

		print("try to guess a letter of the word :")

		letter=input(" : ")
		if letter not in positionned:
			wtries+=1

		tries+=1


		for i in range(len(elWord)):
			if letter == elWord[i]:
				position[letter].append(i)

		print(position)# to retract # admin stuff
			
			# detect when a new letter is entered
		if letter in elWord and letter not in letterRecord:	

			letterFound.append(letter)
			letterRecord.append(letter)

		elif letter not in letterRecord and letter not in elWord:	# record entered characters

			letterRecord.append(letter)

		if len(letterFound)==len(positionned):	# when we win or loose # when game ends
			return("won")
		elif wtries==6:
			return("lost")
#	return 0




#	start time, start game
start_time = time.time()

result=game("chaleté")

print("\nResult : ",result)

end_time = time.time()

time = end_time-start_time
print("\n",time)

