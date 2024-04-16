""" Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked.  """

import random

random_number = random.randint(1,10)
user_number = 0
while random_number != user_number:
    user_number = int(input('Enter a number from 1 to 10: '))
print('Well done, the random number was ->', random_number)
