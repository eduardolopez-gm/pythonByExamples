""" Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.  """

name = input('Enter your name: ')
times = int(input('Enter a number to repeat the name: '))
for i in range(1,times+1):
    for letter in name:
        print(letter)
    print('\n')