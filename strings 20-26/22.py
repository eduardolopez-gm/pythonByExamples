""" Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.  """

name = str.lower(input('Enter your name :'))
lastname = str.lower(input('Enter your lastname :'))
name = name.capitalize()
lastname = lastname.capitalize()
print('Result -> ', name + ' ' + lastname)
