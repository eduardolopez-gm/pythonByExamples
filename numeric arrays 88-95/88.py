""" Ask the user for a list of five integers. Store them in an array.
Sort the list and display it in reverse order.  """
from array import *
from faker import Faker
fake = Faker()

number_array = array ('i', [])
# Generate random integers
for number in range(0,9):
    number_array.append(fake.random_int(10,100))

print('Generated array is:')
print(number_array)

print('Generated Sorted array is:')
sorted_array = sorted(number_array)
print(sorted_array)

print('Generated Reversed array is:')
sorted_array.reverse()
print(sorted_array)