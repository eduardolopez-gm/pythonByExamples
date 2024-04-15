# Task the user to enter a number over 100 and then enter a number under
# 10 and tell them how many times the smaller number goes into the larger
# number in a user-friendly format

high_number = int(input('Enter a number over 100: '))
min_number = int(input('Enter a number above 10: '))
calculation = int(high_number / min_number)
print(min_number,"goes into",high_number,calculation,"times")

