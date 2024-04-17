""" Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.  """

countries = ('Argentina', 'Brazil', 'Colombia', 'Denmark', 'USA')
print(countries)
user_choice = input('Enter a country from the list: ')
index = countries.index(user_choice)
print('The index of the element is -> ', index)
