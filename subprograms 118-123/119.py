""" Define a subprogram that will ask the user to 
pick a low and a high number, and then 
generate a random number between those 
two values and store it in 
a variable called “comp_num”. 

Define another subprogram that will 
give the instruction “I am thinking of a number…” 
and then ask the user to guess the number they 
are thinking of.

Define a third subprogram that will 
check to see if the comp_num is the same 
as the user’s guess. If it is, it should display the 
message “Correct, you win”, otherwise it should
keep looping, telling the user if they are too low or 
too high and asking them to guess again until they 
guess correctly. """
import random

def get_random_number():
    low_bundary = int(input('Enter a number: '))
    high_boundary = int(input('Enter a number higher than the one you enter before: '))
    comp_num = random.randint(low_bundary, high_boundary)
    return comp_num

def get_user_number():
    print('I am thinking of a number…')
    user_number = int(input())
    return user_number

def validate_numbers(random_number, user_number):
    while (random_number != user_number):
        if user_number > random_number:
            print('Try with a lower number')
        elif user_number < random_number:
            print('Try with a higher number')
        user_number = int(input())
    print('Correct, you win')

def main():
    random_number = get_random_number()
    user_number = get_user_number()
    validate_numbers(random_number, user_number)


main()
