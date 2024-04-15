""" Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.  """

name = str(input('Enter your name :'))
lastname = str(input('Enter your lastname :'))
print('Your complete name is ->', name+ ' ' + lastname)
# print(repr(name) + ' ' + repr(lastname))
print('Length of your name is -> ', len(name)+len(lastname))