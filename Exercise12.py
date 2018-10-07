#Exercise 12 - List Ends
#PracticePython.org

from random import sample

def first_last_elems(list_input):
	return print([list_input[0],list_input[-1]])

a = sample(range(100),5)
print(a)

first_last_elems(a)