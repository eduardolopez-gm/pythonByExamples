""" In Python, it is not technically possible to directly 
delete a record from a .csv file. Instead you need 
to save the file to a temporary list in Python, 
make the changes to the list and then overwrite 
the original file with the temporary list. 
Change the previous program to allow you to do 
this. Your menu should now look like this:

1) Add to file 
2) View all records 
3) delete a record 
4) quit program 

Enter the number of your selection:  """




def add_to_file():
    file = open('Salaries.csv', 'a')
    name = input('Enter the name: ')
    salary = input('Enter the salary: ')
    new_record = name + ',' + salary + '\n'
    file.write(str(new_record))
    file.close()

def view_all_records():
    try:
        file = open('Salaries.csv', 'r')
        for row in file:
            print(row)
        file.close()
    except:
        print('Error reading file \n')

def delete_record():
    temp_list = []
    index = 0
    # Create a temporary list to store the records
    file = open('Salaries.csv', 'r')
    for row in file:
        temp_list.append(row)
    file.close()
    # Show the records to the user
    for record in temp_list:
        print(index, record)
        index += 1
    record_to_delete = int(input('Enter the record number to delete: '))
    # Delete the record from the temporary list
    del temp_list[record_to_delete]
    # Write the temporary list to the file
    file = open('Salaries.csv', 'w')
    for record in temp_list:
        file.write(record)
    file.close()


def main():
    while True:
        print('##### MENU #####')
        print('1. Add to file')
        print('2. View all records')
        print('3. Delete a record')
        print('4. Exit')
        print('############## \n')

        option = int(input('Enter an option of the menu: '))
        if option == 1:
            add_to_file()
        elif option == 2:
            view_all_records()
        elif option == 3:
            delete_record()
        elif option == 4:
            break
        else:
            print('Invalid option, try again \n')
        
main()