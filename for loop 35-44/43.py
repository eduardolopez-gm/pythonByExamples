""" Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”.  """

direction = input('Enter a direction(up/down) to count :')
if direction.lower() == 'up':
    top_number = int(input('Enter the top number: '))
    for i in range(1,top_number+1):
        print('Counting -->', i)
elif direction.lower() == 'down':
    below_number = int(input('Enter a number below 20: '))
    if below_number >= 20:
        print('ERROR, invalid value')
    else:
        for i in range(20,below_number-1,-1):
            print('Counting -->', i)
else:
    print('I don\'t understand')