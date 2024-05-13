""" Display the following menu to the user: 
1) Addition 
2) Subtraction 

If they enter a 1, it should run a subprogram that will 
generate two random numbers between 5 and 20, and 
ask the user to add them together. Work out the correct 
answer and return both the user’s answer and the 
correct answer. 

If they entered 2 as their selection on the menu, it 
should run a subprogram that will generate one number 
between 25 and 50 and another number between 1 and 
25 and ask them to work out num1 minus num2. This 
way they will not have to worry about negative answers. 
Return both the user’s answer and the correct answer. 

Create another subprogram that will check if the user’s 
answer matches the actual answer. If it does, display 
“Correct”, otherwise display a message that will say 
“Incorrect, the answer is” and display the real answer. 
If they do not select a relevant option on the first menu 
you should display a suitable message. """
import random

def addition_function():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    real_answer = num1 + num2
    user_answer = int(input('Enter the solution to -> ' + str(num1) + '+' + str(num2) + '= '))
    return real_answer, user_answer

def subtraction_function():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    real_answer = num1 - num2
    user_answer = int(input('Enter the solution to -> ' + str(num1) + '-' + str(num2) + '= '))
    return real_answer, user_answer

def validate_result(real_answer, user_answer):
    if real_answer == user_answer:
        print('Correct')
    else:
        print('Incorrect, the answer is ->'+str(real_answer))

def main():
    print('Welcome to this modular program')
    print('1) Addition')
    print('2) Subtraction')
    user_choice = int(input('Enter an option: '))
    if user_choice not in (1,2):
        print('Error, invalid value')
    elif user_choice == 1:
        real, user = addition_function()
    else:
        real, user = subtraction_function()
    validate_result(real, user)



main()