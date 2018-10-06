#Exercise 5 - List Overlap
#PracticePython.org

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []

for x in a:
	if x in b:
		new_list.append(x)

print(new_list)

new_list = [x for x in list(set(a)) if x in b]

print(new_list)

from secrets import randbelow
from random import sample, randint, random, randrange

# list_1 = [x for x in range(random.randint(1,15),random.randint(15,15*2))]
# print(list_1)

def ran_list(num):
	list_1 = [randrange(num) for x in sample(range(0,randint(num*2,num*4)),randint(0,num))]
	list_2 = [randrange(num) for x in sample(range(0,randint(num*2,num*4)),randint(0,num))]
	unique_list = [x for x in list(set(list_1)) if x in list_2]
	return print(f'List 1 contains: {sorted(list_1)}\n List 2 contains: {sorted(list_2)}\n Unique values: {unique_list}')


ran_list(100)

