# Ask for two numbers. If
# the first one is larger
# than the second, display
# the second number first
# and then the first
# number, otherwise show
# the first number first and
# then the second.


number1 = int(input('Enter two numbers:\n'))
number2 = int(input())

if number1 > number2:
    print('second goes first', number2, number1)
else:
    print('first',number1, number2)
