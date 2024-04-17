""" Create a list of four three-digit numbers. Display the list to the 
user, showing each item from the list on a separate line. Ask the user to enter a three-digit
number. If the number they have typed in matches one in the list, display the position of
that number in the list, otherwise display the message “That is not in the list”.  """
import random

# Create a list of numbers of three digit
number_list = []
for number in range(0,10):
    number_list.append(random.randint(100,999))
# print(number_list, len(number_list))

# Display the list
for number in number_list:
    print(number)

user_number = int(input('Enter a three digit number:  '))
if user_number in number_list:
    print('It\'s a match')
else:
    print('That is not in the list')