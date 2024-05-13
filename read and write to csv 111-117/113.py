""" Using the Books.csv file, ask the user how many records
they want to add to the list and then allow them to add
that many. After all the data has been added, ask for an
author and display all the books in the list by that author.
If there are no books by that author in the list, display a
suitable message.  """
import csv
from faker import Faker
fake = Faker()

file = open ('Books.csv', 'a')
# Generate a random row
records = int(input('Enter the number of records that you want to add to the Books.csv file :'))
for i in range(0,records):
    book_name = fake.sentence(5)
    book_author = fake.name()
    book_published = str(fake.random_int(1960,2020))
    newRecord = book_name+','+book_author+','+book_published+'\n'
    file.write(str(newRecord))
file.close()

# Display the rows of the csv file
file = open('Books.csv', 'r')
for row in file:
    print(row)
file.close()
# Search one author in the csv file
file = open('Books.csv', 'r')
author_search = input('Enter an author name:')
print(author_search)
count = 0
for row in file:
    if author_search in str(row):
        print(row)
        count += 1
if count == 0:
    print('Author not found!')
file.close()