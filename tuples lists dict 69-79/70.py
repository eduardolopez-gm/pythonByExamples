""" Add to program 069 to ask the user to enter a number and
display the country in that position.  """

countries = ('Argentina', 'Brazil', 'Colombia', 'Denmark', 'USA')
print(countries)
user_choice = input('Enter a country from the list: ')
index = countries.index(user_choice)
print('The index of the element is -> ', index)
user_index = int(input('Enter a number from 0 to 4: '))
print('The element on that index is -> ', countries[user_index])