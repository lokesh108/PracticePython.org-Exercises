#Exercise 8 - Rock Paper Scissors
#PracticePython.org

from random import randint

keep_playing = "y"

def get_player_input():
	choices = ["rock","paper","scissors","quit"]
	if single != None:
		return choices[randint(0,3)]
	choice = input(f"Choose from {choices[:3]}: ").lower()
	while choice not in choices:
		print(f"{choice} is not a valid.")
		choice = input(f"Choose from {choices[:3]}, or 'Quit' to exit. ").lower()

	return choice

def quit_early(choice):
	if choice == "quit":
		return True

def decalre_winner(player1,player2):
	if player1 == player2:
		return print(f"Draw!  You both chose {player1}!")
	if player1 == "rock" and player2 == "scissors":
		return print(f"Player 1 wins with {player1} over Player 2's {player2}!")
	elif player1 == "scissors" and player2 == "paper":
		return print(f"Player 1 wins with {player1} over Player 2's {player2}!")
	elif player1 == "paper" and player2 == "rock":
		return print(f"Player 1 wins with {player1} over Player 2's {player2}!")
	else:
		return print(f"Player 2 wins with {player2} over Player 1's {player1}!")

while keep_playing == "y":
	single = input("Play against computer?  Y/N: ").lower()
	player_1 = get_player_input()
	if quit_early(player_1):
		break
	if quit_early(player_1):
		break
	if single == "y":
		player_2 = get_player_input(single)
	else:
		player_2 = get_player_input()
		if quit_early(player_2):
			break
	decalre_winner(player_1,player_2)
	keep_playing = input("Play again? Y/N: ").lower()


print("Thanks for playing!")
