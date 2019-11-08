from gameFunctions import gameSykes

# need a function to run to compare the choices
# figure out what to pass into the function - hint => what are you comparing?
def compareChoices():

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
			print("You win!", player, "cuts", gameSykescomputer, "\n")
			gameSykes.computer_lives = gameSykes.computer_lives - 1 