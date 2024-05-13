""" Using the Books.csv file from program 111, ask
the user to enter another record and add it to the
end of the file. Display each row of the .csv file
on a separate line.  """
import csv
from faker import Faker
fake = Faker()

file = open('Books.csv', 'a')
# Generate a random data
for i in range(0,3):
    book_name = fake.sentence(5)
    book_author = fake.name()
    book_published = str(fake.random_int(1960,2020))
    newRecord = book_name+','+book_author+','+book_published+'\n'
    file.write(str(newRecord))
file.close()
file = open('Books.csv', 'r')
for row in file:
    print(row)
