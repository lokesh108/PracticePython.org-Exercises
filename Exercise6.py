#Exercise 6 - String Lists
#PracticePython.org

user_input = input('Provide any word you want. ')

if user_input[::-1].lower() == user_input.lower():
	print('That word is a palindrome!')
else:
	print(user_input[::-1])