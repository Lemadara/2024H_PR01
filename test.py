import os
from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
import random
import time
print(" hello ")

#import keyboard

#	A = lire_dictionnaires_mots()
#	print(A["facile"])

"""	
	print(" test 1")
	tries=0
	listE=[]
	###

	multi=len(elWord)
	listW=elWord.split()

	###
	print(" test 1.1")

	letter=input("give a letter")
	print(" test 2")

	if letter not in listE and letter in listW:
		listE.append(letter)
		tries+=1
		print(" test C1")

	if letter in listW:
		position=listW.index(letter)
		print(" test C2")

	else:
		print("error try again with a real letter")
		print(" test c3")

	while True:
		print(f"mots:"+"_"*multi)
		print(f"lettre trouvé:"+listW[position])
		print(f"")
		print(f"")
		print(f"")
		print(f"")
		print(f"")

	"""

def game(elWord):
	
	###	Game starts
	position={}	
	positionned=[]
	for x in elWord:
		if x not in positionned:
			position[x]=[]
			positionned.append(x)
	letterFound=[]
	letterRecord=[]

	tries=0

	h='O'
	b='|'
	l,r='/',"\\"


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


		if tries==0:

			print("")
			print("  +---+")
			print("  |   |")
			print(f"  {' '}   |")
			print(f" {' '}{' '}{' '}  |")
			print(f" {' '} {' '}  |")
			print("         ")
			print("=========")
		elif tries==1:

			print("")
			print("  +---+")
			print("  |   |")
			print(f"  {'O'}   |")
			print(f" {' '}{' '}{' '}  |")
			print(f" {' '} {' '}  |")
			print("         ")
			print("=========")
		elif tries ==2:

			print("")
			print("  +---+")
			print("  |   |")
			print(f"  {'O'}   |")
			print(f" {' '}{'|'}{' '}  |")
			print(f" {' '} {' '}  |")
			print("         ")
			print("=========")
		elif tries ==3:

			print("")
			print("  +---+")
			print("  |   |")
			print(f"  {'O'}   |")
			print(f" {'/'}{'|'}{' '}  |")
			print(f" {' '} {' '}  |")
			print("         ")
			print("=========")
		elif tries ==4:

			print("")
			print("  +---+")
			print("  |   |")
			print(f"  {'O'}   |")
			print(f" {'/'}{'|'}{'\\'}  |")
			print(f" {' '} {' '}  |")
			print("         ")
			print("=========")
		elif tries ==5:

			print("")
			print("  +---+")
			print("  |   |")
			print(f"  {'O'}   |")
			print(f" {'/'}{'|'}{'\\'}  |")
			print(f" {'/'} {' '}  |")
			print("         ")
			print("=========")
		elif tries ==6:

			print("")
			print("  +---+")
			print("  |   |")
			print(f"  {'O'}   |")
			print(f" {'/'}{'|'}{'\\'}  |")
			print(f" {'/'} {'\\'}  |")
			print("         ")
			print("=========")




		print("try to guess a letter of the word :")

		letter=input(" : ")
		tries+=1




		for i in range(len(elWord)):
			if letter == elWord[i]:
				position[letter].append(i)

		print(position)# to retract # admin stuff

		if letter in elWord and letter not in letterRecord:

			letterFound.append(letter)
			letterRecord.append(letter)

		elif letter not in letterRecord and letter not in elWord:

			letterRecord.append(letter)

		if len(letterFound)==len(positionned):
			return("won")
		elif tries==6:
			return("lost")
			

	### test before implanting

	
	return 0


start_time = time.time()

result=game("chaleté")
print("\nResult : ",result)
end_time = time.time()
time = end_time-start_time
print("\n",time)