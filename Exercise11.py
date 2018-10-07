#Exercise 11 - Check Primality Functions
#PracticePython.org

def check_prime(num):
	divisors = [x for x in range(2,num) if num % x == 0]
	if len(divisors) > 0:
		return print(f"The divisors for {num} are {divisors}.")
	else:
		return print("That number is prime!")


num = int(input("Please choose any number. "))

check_prime(num)