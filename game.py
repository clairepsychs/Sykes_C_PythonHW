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

	# always check a breaking condition first
	if player == gameSykes.computer:
		#we have a tie, no point in going any further
		print("tie, no one wins! try again")
		
	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if gameSykes.computer == "paper":
			print("You lose!", gameSykes.computer, "covers", player, "\n")
			gameSykes.player_lives = gameSykes.player_lives - 1
		else:
			print("You won!", player,"smashes", gameSykes.computer, "\n")
			gameSykes.computer_lives = gameSykes.computer_lives - 1 

	elif player == "paper":
		if gameSykes.computer == "scissors":
			print("You lose!", gameSykes.computer, "cuts", player, "\n")
			gameSykes.player_lives = gameSykes.player_lives - 1
		else:
			print("You won!", player, "covers", gameSykes.computer, "\n")
			gameSykes.computer_lives = gameSykes.computer_lives - 1 

	elif player == "scissors":
		if gameSykes.computer == "rock":
			print("You lose!", gameSykes.computer, "smashes", player, "\n")
			gameSykes.player_lives = gameSykes.player_lives - 1
		else:
			print("You win!", player, "cuts", gameSykes.computer, "\n")
			gameSykes.computer_lives = gameSykes.computer_lives - 1 

	if gameSykes.player_lives is 0:
		winlose.winorlose("lost")		

	elif gameSykes.computer_lives is 0:
		winlose.winorlose("Won")
		# print("You won! Play Again?")


	player = False
	gameSykes.computer=gameSykes.weapons[randint(0,2)]