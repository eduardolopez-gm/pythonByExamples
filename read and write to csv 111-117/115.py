""" Using the Books.csv file, display the data in
the file along with the row number of each. """
import csv

file = open('Books.csv', 'r')
index = 0
for row in file:
    print('Row', index, '->', row)
    index += 1
file.close()