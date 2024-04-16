""" Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.  """

people_invited = int(input('Enter the number of people that you invited: '))
if people_invited >= 10:
    print('Too many people')
else:
    for i in range(0,people_invited):
        name_of_invited = input('Enter the name of your pal: ')
        print(name_of_invited.upper(), ' has been invited.')