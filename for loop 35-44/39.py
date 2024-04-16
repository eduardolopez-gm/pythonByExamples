""" Ask the user to enter a number between 1
and 12 and then display the times table for
that number.  """

number = int(input('Enter a number between 1 to 12: '))
if number>0 and number <= 12:
    for i in range (1,13):
        result = i * number
        print(i, 'x', number, '=', result)
else:
    print('ERROR, invalid value')