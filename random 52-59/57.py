""" Update program 056 so that it tells the user if they
are too high or too low before they pick again.  """

import random

random_number = random.randint(1,10)
user_number = int(input('Enter a number from 1 to 10: '))
while random_number != user_number:
    if user_number > random_number:
        print('Too high, try again')
    elif user_number < random_number:
        print('Too low, try again')
    user_number = int(input('Enter a number from 1 to 10: '))
    
print('Well done, the random number was ->', random_number)

