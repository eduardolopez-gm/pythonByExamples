""" Create an array of five numbers between 10 and 100 which each have
two decimal places. Ask the user to enter a whole number between 2 and 5.
If they enter something outside of that range, display a suitable error message
and ask them to try again until they enter a valid amount. Divide each of the
numbers in the array by the number the user entered and display the answers
shown to two decimal places.  """
from array import *
from faker import Faker
fake = Faker()

numbers_array = array('f', [])

# Create an array of random integers
for i in range(0,5):
    random_number = fake.random_int(10,100)
    numbers_array.append(random_number)
print('Generated array is -> ', numbers_array)
number = int(input('Enter a number from 2 to 5 :'))
while number < 2 and number > 5:
    print('Value out of range')
    number = int(input('Enter a number from 2 to 5 :'))
print('Result of divide array with the number you provide')
for index in numbers_array:
    result = index/number
    print('%.2f' % result)


