#Exercise 4 - Divisors
#PracticePython.org

num = int(input("Please choose a number. "))

def divisors(num):
	rng = range(2,num)
	return [x for x in rng if num % x == 0]

print(divisors(num))