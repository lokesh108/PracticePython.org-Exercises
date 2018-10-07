#Exercise 15 - Reverse Word Order
#PracticePython.org

def reverse_string(string):
	splitString = string.split()
	print(splitString)
	reverse = [splitString[-x] for x in range(1,len(splitString)+1)]
	print(reverse)
	result = " ".join(reverse)
	return print(result)

reverse_string("This is a string")

#after seeing other's code - revising for better solution
#https://gist.github.com/jefnic23/a9e21b5d27d9ab5ba76d

def reverse_string_revised(string):
	reverse = string.split()[::-1]
	return " ".join(reverse)

print(reverse_string_revised("This is a string"))