#Exercise 9 - Guessing Game One
#PracticePython.org

from random import randint

def get_user_guess():
	guess = int(input("Pick a number between 1 and 9. "))
	if guess not in range(1,10):
		print("Number was not a valid guess.  Please try again. ")
		get_user_guess()

	return guess


numToGuess = randint(1,9)

print("Are you ready to please the game?")

userGuesses = []

while numToGuess not in userGuesses:
	guess = get_user_guess()
	if guess in userGuesses:
		print("You have already guessed that number!")
	else:
		if guess > numToGuess:
			print("Your guess was too high!")
		elif guess < numToGuess:
			print("Your guess was too low!")
		elif guess == numToGuess:
			print("You guessed correctly!")
		userGuesses.append(guess)

	

	print(userGuesses)

