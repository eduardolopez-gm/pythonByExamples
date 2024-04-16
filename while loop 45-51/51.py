""" Using the song “10 green bottles”, display the lines “There are [num] green bottles
hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
should accidentally fall”. Then ask the question “how many green bottles will be
hanging on the wall?” If the user answers correctly, display the message “There will be
[num] green bottles hanging on the wall”. If they answer incorrectly, display the
message “No, try again” until they get it right. When the number of green bottles gets
down to 0, display the message “There are no more green bottles hanging on the wall”.  """

num = 10

while num > 0:
    print('There are ', num, ' green bottleshanging on the wall')
    print(num,' green bottles hanging on the wall')
    print('and if 1 green bottle should accidentally fall')
    answer = int(input('How many green bottles will be hanging on the wall? '))
    num -= 1
    if answer == num:
        print('There will be ', num, ' green bottles hanging on the wall\n')
    else:
        print('--> Nop, try again\n  <--')
print('There are no more green bottles hanging on the wall')
