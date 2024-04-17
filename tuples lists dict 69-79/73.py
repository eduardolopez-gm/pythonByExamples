""" Ask the user to enter four of their favourite foods and store them in
a dictionary so that they are indexed with numbers starting from 1. Display
the dictionary in full, showing the index number and the item. Ask
them which they want to get rid of and remove it from the list. Sort
the remaining data and display the dictionary.  """

from operator import index


favorite_food = {}
for i in range(1,5):
    user_food = input('Enter your favorite food:  ')
    favorite_food[i] = user_food

print(favorite_food)

del_food = int(input('Which food would you like to remove? (1-4) '))

print(favorite_food.keys())
print(favorite_food.values())

del favorite_food[del_food]
print(sorted(favorite_food.values()))