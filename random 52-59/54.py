""" Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails. 
 """
import random
choices = ['h', 't']
random_selected = random.choice(choices)
user_choice = input('Select "h"eads or "t"ails: ')
if random_selected == user_choice:
    print('You win')
else:
    print('Bad luck')
print('The random value is ->', random_selected)
