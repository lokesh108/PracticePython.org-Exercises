#Exercise 3 - List Less Than Ten
#PracticePython.org

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
mylist = []

for thing in a:
	if thing < 5:
		mylist.append(thing)
		
print(mylist)

mylist = [x for x in a if x < 5 ]

print(mylist)

user_num = int(input("Please choose a number. "))

mylist = [x for x in a if x < user_num]

print(mylist)