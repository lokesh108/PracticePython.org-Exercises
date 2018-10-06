#Exercise 1 - Character Input
#PracticePython.org

import datetime

name = input('Please provide your name. ')
age = int(input('What is your age?'))
turn100 = datetime.datetime.now().year + (100 - age)
printTimes = int(input('Please provide a number. '))
print(('Hello ' + name + '.  You will turn 100 years old in ' + str(turn100) + '\n') * printTimes)
