""" Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.  """
from faker import Faker
fake = Faker()

file = open("Names.txt", "w")
for i in range(0,9):
    random_name = fake.first_name()
    file.write(random_name+'\n')
file.close()