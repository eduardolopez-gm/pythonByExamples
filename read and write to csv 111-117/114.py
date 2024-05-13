""" Using the Books.csv file, ask the user to enter a starting year and an end
year. Display all books released between those two years. """
import csv
from faker import Faker
fake = Faker()
# Generate random start and end year
starting_year = fake.random_int(1813,1900)
end_year = fake.random_int(1900,2000)
print(starting_year, end_year)

# Convert csv file to a list
file = list(csv.reader(open('Books.csv')))

for row in file:
    # condition to show data
    if int(row[2]) >= starting_year and int(row[2]) <= end_year:
        print(row)




