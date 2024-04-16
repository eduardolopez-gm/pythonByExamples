""" Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
“Correct”, otherwise display “You lose”. """

import random

random_number = random.randint(1,5)
user_number = int(input('Choose a number between 1 to 5: '))
if user_number == random_number:
    print('Well done')
elif user_number > random_number:
    print('Too high')
else:
    print('Too low')
user_number = int(input('Choose another number from 1 to 5: '))
if user_number == random_number:
    print('Correct')
else:
    print('You lose, the random number was ->', random_number)