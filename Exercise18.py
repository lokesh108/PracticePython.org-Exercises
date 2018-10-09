#Exercise 17 - Decode a Webpage
#PracticePython.org

from random import randint

the_number = str(randint(1000,10000))
guessed_dict = {}
keep_playing = True

def user_guess(num):
	guess = input("Choose a 4 digit number. ")
	if guess == "giveme":
		return print(num)
	if not guess.isdigit():
		return print("That was not a number!")
	cows = 0
	bulls = 0
	this_index = len(guessed_dict)+1
	if guess == num:
		return True, print(f"{guess} was correct!  It took you {this_index} tries.")
	for x in range(4):
		if guess[x] == num[x]:
			cows += 1
		elif guess[x] in num:
			bulls += 1
	guessed_dict[this_index] = {"Guess":guess,"Cows":cows,"Bulls":bulls}
	for key, val in guessed_dict.items():
		print(key, val)

while keep_playing:
	# user_guess(the_number)
	if user_guess(the_number):
		play_again = input("Would you like to play again?  Y/N: ").lower()
		if play_again == "n":
			keep_playing = False
		else:
			the_number = str(randint(1000,10000))
			guessed_dict = {}
			number_found = False

print("Thank you for playing!")