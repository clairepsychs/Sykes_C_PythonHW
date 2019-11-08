from random import randint

weapons=["rock", "paper", "scissors"]

#adding lives -> when one or the other gets 0, win/lose
player_lives = 1
computer_lives = 1

total_lives = 1

# Let the AI make a choice
computer=weapons[randint(0,2)]

# set up a game loop here so we don't have to keep restarting
player = False