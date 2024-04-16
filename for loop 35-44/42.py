""" Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.  """

total = 0
for i in range(1,6):
    number = int(input('Enter a number: '))
    include_number = input('Do you want to include this number? (yes/no) ')
    if include_number.lower() == 'yes':
        total += number

print('Total result is -> ', total)