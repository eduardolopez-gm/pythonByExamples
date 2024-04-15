# Ask how many slices
# of pizza the user
# started with and ask
# how many slices
# they have eaten.
# Work out how many
# slices they have left
# and display the
# answer in a user-
# friendly format.

slices_start = int(input('Please enter how many pizza slices you have\n'))
slices_eaten = int(input('Please enter how many slices you have eat\n'))
slices_finish = slices_start - slices_eaten
print('You have left' , slices_finish, 'slices')