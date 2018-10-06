#Exercise 2 - Odd or Even
#PracticePython.org

num = int(input('Choose a number. '))

if num % 2 == 0:
	print('That is an even number!')
else:
	print('That is an odd number!')

num = int(input('Choose a new number. '))

if num % 4 == 0:
	print('Thinking in quarters I see...')
elif num % 2 == 0:
	print('Just a regular even number.')
else:
	print("Your're a bit odd!")

num = int(input('Choose a final number. '))
check = int(input('I lied, give me another number. '))

if num % check == 0:
	print('You seek balance in the force.')
else:
	print('Are you always the remainder?')