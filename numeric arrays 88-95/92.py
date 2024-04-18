""" Create two arrays (one containing three numbers that
the user enters and one containing a set of five random
numbers). Join these two arrays together into one large array.
Sort this large array and display it so that each number appears
on a separate line.  """
from array import *
from faker import Faker
fake = Faker()

numbers_array1 = array('i', [])
numbers_array2 = array('i', [])

# Create an array of random integers
for i in range(0,3):
    random_number = fake.random_int(1,100)
    numbers_array1.append(random_number)
# Create an array of random integers
for i in range(0,9):
    random_number = fake.random_int(1,100)
    numbers_array2.append(random_number)
# Check values of different arrays
print(numbers_array1, numbers_array2)

# join 2 arrays
numbers_array1.extend(numbers_array2)
print(numbers_array1)
# sorted the result of 2 arrays
numbers_array1 = sorted(numbers_array1)
print(numbers_array1)