""" Create an array which contains five numbers (two of which
should be repeated). Display the whole array to the user. Ask
the user to enter one of the numbers from the array and
then display a message saying how many times that number
appears in the list. """
from array import *
from faker import Faker
fake = Faker()

numbers_array = array('i', [])
# Create an array of random integers
for i in range(0,9):
    random_number = fake.random_int(1,100)
    numbers_array.append(random_number)
print(numbers_array)

# Get one of the elements and duplicate in the array
duplicate_number = numbers_array[3]
numbers_array.append(duplicate_number)

print(numbers_array)
print('Element',duplicate_number ,'appears ', numbers_array.count(duplicate_number), 'times in the array')
