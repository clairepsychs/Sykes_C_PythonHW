from random import randint
from gameFunctions import gameSykes

def winorlose(status):
	print("called win or lose function", status,"\n")
	print("You", status, "! Would you like to play again?")
	choice = input ("Y / N? ")

	if choice == "Y" or choice == "y":
		# reset the game and start all over again
		gameSykes.player_lives = 1
		gameSykes.computer_lives = 1
		gameSykes.player - False
		gameSykes.computer = gameSykes.weapons[randint(0,2)]
		
	elif choice == "N" or choice == "n":
			print("You chose to quit. Better luck next time!")
			exit()	
	else:
		print("Make a valid choice. Yes or no!")
		# recursion function => calling a function from inside itself
		winorlose(status)