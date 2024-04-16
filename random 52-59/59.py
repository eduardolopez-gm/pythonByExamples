""" Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly.  """

import random

colors = ['blue', 'green', 'yellow', 'grey', 'red']
random_color = random.choice(colors)
print('We have ', colors, 'colors, pick one')
user_answer = input()
while random_color != user_answer:
    if random_color == 'green':
        print('I bet you are GREEN with envy')
    elif random_color == 'blue':
        print('You are probably feeling BLUE right now')
    elif random_color == 'yellow':
        print('I bet you are YELLOW with hungry')
    elif random_color == 'grey':
        print('I bet you are GREY with envy')
    else:
        print('You are probably feeling RED right now')
    user_answer = input()
print('Well, done')