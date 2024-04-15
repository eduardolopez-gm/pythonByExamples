# Ask for the total price of the bill, then ask how
# many diners there are. Divide the total bill by the
# number of diners and show how much each
# person must pay.

bill = int(input('Enter total bill: '))
people = int(input('Enter diners: '))
bill_per_diner = bill / people
print('Each diner must pay', bill_per_diner)