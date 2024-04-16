""" Ask the user to enter a
number and then enter
another number. Add these
two numbers together and
then ask if they want to add
another number. If they
enter “y", ask them to enter
another number and keep
adding numbers until they
do not answer “y”. Once the
loop has stopped, display
the total.  """

number1 = int(input('Enter a number: '))
number2 = int(input('Enter another number: '))
total = number1 + number2
end_condition = input('Do you want to add more numbers? (y/n)')
end_condition = end_condition.lower()
while end_condition == 'y':
    number1 = int(input('Enter a number: '))
    total += number1
    end_condition = input('Do you want to add more numbers? (y/n)')
    end_condition = end_condition.lower()
print('Total is -> ', total)