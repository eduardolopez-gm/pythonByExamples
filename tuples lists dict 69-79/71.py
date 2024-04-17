""" Create a list of two sports. Ask the user what their favourite sport is and
add this to the end of the list. Sort the list and display it.  """

sports = ['Football', 'Basketball']
user_sport = input('Enter your favorite sport: ')
sports.append(user_sport)
sports_sorted = sorted(sports)
print('Original list ',sports)
print('Sorted list ',sports_sorted)