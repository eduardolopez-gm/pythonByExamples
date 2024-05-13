""" Define a subprogram that will ask the user to 
enter a number and save it as the variable 
“num”. Define another subprogram that will 
use “num” and count from 1 to that number """

def ask_a_number():
    number = int(input('Enter a number: '))
    return number

def number_plus_one(number):
    return number + 1

def main():
    user_number = ask_a_number()
    print(number_plus_one(user_number))


main()