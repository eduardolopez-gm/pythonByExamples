""" Using the Names.txt file you created earlier, display the list of
names in Python. Ask the user to type in one of the names and then
save all the names except the one they entered into a new file called
Names2.txt.  """
import os 
# Display the list
file = open('Names.txt', 'r')
print(file.read())
file.close()
# Remove the new file if already exist
if os.path.exists('Names2.txt'):
    os.remove('Names2.txt')

name = input('Enter a name from the list : ')
name = name + '\n'

file = open('Names.txt', 'r')
# Create a new file without the selected name
for row in file:
    if row != name:
        new_file = open('Names2.txt', 'a')
        new_file.write(row)
        new_file.close()
file.close()

file = open('Names2.txt', 'r')
print(file.read())

