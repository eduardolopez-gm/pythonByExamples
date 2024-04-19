""" Display the following menu to the user:

1) Create a new file
2) Display the file
3) Add a new item to the file

Ask the user to enter 1, 2 or 3.
If they select anything other than 1, 2 or 3 it should display a
suitable error message.
If they select 1, ask the user to enter a school subject and save it to a new file called
“Subject.txt”. It should overwrite any existing file with a new file.
If they select 2, display the contents of the “Subject.txt” file.
If they select 3, ask the user to enter a new subject and save it to the file and then display
the entire contents of the file.
Run the program several times to test the options. """

print('#########################')
print('1) Create a new file')
print('2) Display the file')
print('3) Add a new item to the file')
print('#########################')
option = int(input('Enter an option from 1 to 3:  '))

if option < 1 or option > 3:
    print('ERROR, value out of range')
else:
    if option == 1:
        subject = input('Enter a school subject:  ')
        file = open('Subject.txt', 'w')
        file.write(subject+'\n')
    elif option == 2:
        file = open('Subject.txt', 'r')
        print(file.read())
    else: 
        subject = input('Enter another school subject:  ')
        file = open('Subject.txt', 'a')
        file.write(subject+'\n')
        file.close()
        file = open('Subject.txt', 'r')
        print(file.read())
file.close()
