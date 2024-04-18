""" Create an array which will store a list of integers.
Generate five random numbers and store them in
the array. Display the array (showing each item on
a separate line).  """
from array import *
from faker import Faker
fake = Faker()

number_array = array ('i', [])
# Generate random integers
for number in range(0,9):
    number_array.append(fake.random_int(10,10000))

for number in number_array:
    print(number)
