""" Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”.  """

compnum = 50
number = int(input('Can you guess a number? '))
attempts = 1
while compnum != number:
    if compnum > number:
        print('Too low, try again')
    elif compnum < number:
        print('Too high, try again')
    attempts += 1
    number = int(input('Enter a number: '))
print('Well done, you took ', attempts, ' attempts')
