""" Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array,
otherwise display the message “Outside the range”. Once five numbers have been
successfully added, display the message “Thank you” and display the array with each item shown
on a separate line. """
from array import *
from faker import Faker
fake = Faker()

numbers_array = array ('i', [])

while (len(numbers_array)) < 10:
    random_number = fake.random_int(10,60)
    if random_number >= 10 and random_number <=20:
        numbers_array.append(random_number)
    else:
        print('Outside the range')
print('Generated array of numbers, Thank you')
for number in numbers_array:
    print(number)



