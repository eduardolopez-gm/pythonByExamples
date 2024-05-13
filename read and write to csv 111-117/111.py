""" Create a .csv file that will store the following data. Call it “Books.csv”.

  | Book | Author | Year | Released
0 | To Kill A Mockingbird | Harper Lee | 1960
1 | A Brief History of Time | Stephen Hawking | 1988
2 | The Great Gatsby | F. Scott Fitzgerald | 1922
3 | The Man Who Mistook His Wife for a Hat | Oliver Sacks | 1985
4 | Pride and Prejudice | Jane Austen | 1813  
"""

import csv

file = open('Books.csv', 'w')

for book in range(0,5):
    if book == 0:
        newRecord = "To Kill A Mockingbird,Harper Lee,1960\n"
    elif book == 1:
        newRecord = "A Brief History of Time,Stephen Hawking,1988\n"
    elif book == 2:
        newRecord = "The Great Gatsby,F. Scott Fitzgerald,1922\n"
    elif book == 3:
        newRecord = "The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\n"
    elif book == 4:
        newRecord = "Pride and Prejudice,Jane Austen,1813\n"
    file.write(str(newRecord))
file.close() 
