#Exercise 16 - Password Generator
#PracticePython.org

import string
from random import randint, sample

def generate_password(weakness = "Strong"):
	charPool = "".join(string.ascii_letters + string.digits + "!@#$%?")
	if weakness == "Weak":
		result = "".join(sample(charPool,8))
	elif weakness == "Medium":
		result = "".join(sample(charPool,randint(9,12)))
	else:
		result = "".join(sample(charPool,randint(13,16)))
	return result

print(generate_password("Weak"))