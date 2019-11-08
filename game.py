# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameSykes

while gameSykes.player is False:
	print("==============================")
	print("Computer Lives:", gameSykes.computer_lives, "/", gameSykes.total_lives)
	print("Player Lives:", gameSykes.player_lives, "/", gameSykes.total_lives)
	print("==============================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper, scissors: \n")

	# start doing some logic and condition checking
	# print("computer: ", computer, "player: ", player)
	
	# --- This is where you would do the compare stuff
	# --- end compare stuff

	if gameSykes.player_lives is 0:
		winlose.winorlose("lost")		

	elif gameSykes.computer_lives is 0:
		winlose.winorlose("Won")
		# print("You won! Play Again?")


	player = False
	gameSykes.computer=gameSykes.weapons[randint(0,2)]