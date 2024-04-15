""" Display the following message:

1) Square
2) Triangle
Enter a number :

If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.  """

print ('##### Area Calculator ####')
print(' 1) Square')
print(' 2) Triangle')
print('Enter a number :')
print ('###################')
option= int(input('Enter one option: '))
if option == 1:
    side = int(input('Enter the length of one side: '))
    area = side ** 2
    print('Area of Square is -> ', area)
elif option == 2:
    base = int(input('Enter the base: '))
    height = int(input('Enter the height: '))
    area = 1/2 * (base * height)
    print('Area of triangle is ->', area)
else:
    print('ERROR, invalid option')