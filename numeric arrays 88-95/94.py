""" Display an array of five numbers. Ask the user to
select one of the numbers. Once they have selected a
number, display the position of that item in the
array. If they enter something that is not in
the array, ask them to try again until they select a
relevant item.  """
from array import *
from faker import Faker
fake = Faker()

numbers_array = array('i', [])

# Create an array of random integers
for i in range(0,5):
    random_number = fake.random_int(1,100)
    numbers_array.append(random_number)
print('Generated array is -> ', numbers_array)

number = int(input('Select one element '))
correct = False
while correct != True:
    if number in numbers_array:
        print('The index of this element is ->', numbers_array.index(number))
        correct = True
    else:
        print('That element is not in the array')
        number = int(input('Select one element '))
