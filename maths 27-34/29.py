""" Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two decimal places.  """
import math

number = int(input('Enter a number over 500 :'))
if number > 500:
    number_square_root = math.sqrt(number)
    print(round(number_square_root, 2))
else: 
    print('ERROR, wrong value')