#Exercise 13 - Fibonacci
#PracticePython.org


def fibonacci():
	fib = [1,1]
	num = int(input("How many Fibonacci numbers do you want to see?  "))
	# for x in range(2,num):
	# 	fib.append(fib[-2] + fib[-1])

	return print([fib.append(fib[-2] + fib[-1]) for x in range(2,num)])

fibonacci()