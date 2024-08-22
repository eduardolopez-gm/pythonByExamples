""" Create the following menu: 
1) Add to file 
2) View all records 
3) Quit program 

If the user selects 1, allow them to add to a file 
called Salaries.csv which will store their name 
and salary. If they select 2 it should display all 
records in the Salaries.csv file. If they select 3 it 
should stop the program. If they select an 
incorrect option they should see an error 
message. They should keep returning to the 
menu until they select option 3. """

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
    
def main():
    while True:
        print('##### MENU #####')
        print('1. Add to file')
        print('2. View all records')
        print('3. Exit')
        print('############## \n')

        option = int(input('Enter an option of the menu: '))
        if option == 1:
            add_to_file()
        elif option == 2:
            view_all_records()
        elif option == 3:
            break
        else:
            print('Invalid option, try again \n')
        
main()