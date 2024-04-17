""" Enter a list of ten colours. Ask the user for a starting
number between 0 and 4 and an end number between 5 and 9. Display
the list for those colours between the start and end numbers the user input.  """
import random

colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange', 'grey', 'white', 'black', 'pink']
for i in range(0,5):
    start_index = random.randint(0,4)
    end_index = random.randint(5,9)
    print('You select this elements from the list')
    print(colors[start_index:end_index], '\n')


#Original solution
#start_index = int(input('Enter a number from 0 to 4:  '))
#end_index = int(input('Enter a number from 5 to 9:  '))
#print('You select this elements from the list')
#print(colors[start_index:end_index])