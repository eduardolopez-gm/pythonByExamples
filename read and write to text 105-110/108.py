""" Open the Names.txt file. Ask the user to input a
new name. Add this to the end of the file and
display the entire file.  """

file = open('Names.txt', 'a')
new_name = input('Enter a name to append to the file:  ')
file.write(new_name+'\n')
file.close()