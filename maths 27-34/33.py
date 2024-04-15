""" Ask the user to enter two numbers.
Use whole number division to divide
the first number by the second and
also work out the remainder and
display the answer in a user-friendly
way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1
remaining”).  """

number1 = int(input('Enter one number: '))
number2 = int(input('Enter another number: '))
if number1 < number2:
    print('ERROR, division cannot be performed')
elif number2 == 0:
    print('ERROR, division by 0 cannot be performed')
else:
    division = number1 // number2
    remainder = number1 % number2
    print(number1, ' divided by ', number2, ' is ', division, ' with ', remainder, ' reamining.')
