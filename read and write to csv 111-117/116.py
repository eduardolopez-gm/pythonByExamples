""" Import the data from the Books.csv file into a list. Display the
list to the user. Ask them to select which row from the list
they want to delete and remove it from the list. Ask the user
which data they want to change and allow them to change it.
Write the data back to the original .csv file, overwriting the
existing data with the amended data.  """
import csv 
# Convert csv file to a list
file = list(csv.reader(open('Books.csv')))

temp = []

for row in file:
    temp.append(row)
    print(row)

print('Enter a row number that you want to delete from the file, 0 to ', len(file)-1)
delete_row = int(input())
del temp[delete_row]

print('Enter a row number that you want to modify from the file, 0 to ', len(file)-2
      )
alter_row = int(input())

for element in temp[alter_row]:
    print(element)
part = int(input('Which part do you want to modify? 0 to 2 :'))
new_data = input('Enter new data :')
temp[alter_row][part] = new_data


index = 0
file = open('Books.csv', 'w')
for row in temp:
    record = temp[index][0]+','+temp[index][1]+','+temp[index][2]+'\n'
    file.write(record)
    index += 1
file.close()
