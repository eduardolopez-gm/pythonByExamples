""" Create a program that will allow the user to easily manage a list of names. You should 
display a menu that will allow them to add a name to the list, change a name in the 
list, delete a name from the list or view all the names in the list. There should also be a 
menu option to allow the user to end the program. If they select an option that is not 
relevant, then it should display a suitable message. After they have made a selection 
to either add a name, change a name, delete a name or view all the names, they 
should see the menu again without having to restart the program. The program 
should be made as easy to use as possible. 
 """

names = []

def add_name():
    name = input('Enter a name: ')
    names.append(name)

def change_name():
    print(names)
    user_choice = input('Enter the name that you want to change: ')
    try:
        index = names.index(user_choice)
        new_name = input('Enter the new name: ')
        names[index] = new_name
    except ValueError:
        print('Name not found, try again \n')

def delete_name():
    print(names)
    index_to_delete = int(input('Enter the index of the name that you want to delete: '))
    try:
        del names[index_to_delete]
    except IndexError:
        print('Index out of range, try again \n')

def show_names():
    print('======  Names in the list ======')
    for name in names:
        print(name)
    print('======  END of the list ======\n')

def main():
    while True:
        print('##### MENU #####')
        print('1. Add a name')
        print('2. Change a name')
        print('3. Delete a name')
        print('4. View all the names')
        print('5. Exit')
        print('############## \n')

        option = int(input('Enter an option of the menu: '))
        if option == 1:
            add_name()
        elif option == 2:
            change_name()
        elif option == 3:
            delete_name()
        elif option == 4:
            show_names()
        elif option == 5:
            break
        else:
            print('Invalid option, try again \n')
        
main()