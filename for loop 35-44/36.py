""" Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times. """

name = input('Enter your name: ')
times = int(input('Enter a number to repeat the name: '))
for i in range(1,times+1):
    print(name)