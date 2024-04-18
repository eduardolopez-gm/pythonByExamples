""" Ask the user to enter five numbers. Sort them into order
and present them to the user. Ask them to select one of the
numbers. Remove it from the original array and save it in a
new array.  """
from array import *
from faker import Faker
fake = Faker()


numbers_array = array('i', [])
rest_array = array('i', [])

# Create an array of random integers
for i in range(0,9):
    random_number = fake.random_int(1,100)
    numbers_array.append(random_number)
print('Generated array is -> ', numbers_array)
numbers_array = sorted(numbers_array)
print('Generated array sorted is -> ', numbers_array)

user_response = int(input('Select one value from the array '))
rest_array.append(user_response) 
numbers_array.remove(user_response)
print('Generated array sorted is -> ', numbers_array)
print('Rest array is -> ', rest_array)