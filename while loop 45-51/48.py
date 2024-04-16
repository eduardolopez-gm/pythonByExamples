""" Ask for the name of somebody the user wants to invite
to a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
they want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
coming to the party.  """

count = 0
invited_name = input('Can yo tell me the name of your invite? ')
print(invited_name, ' has been invited')
count += 1
end_condition = input('Do you want to invite someone else? (y/n)')
while end_condition == 'y':
    invited_name = input('Can yo tell me the name of your invite? ')
    print(invited_name, ' has been invited')
    count += 1
    end_condition = input('Do you want to invite someone else? (y/n)')
print('Total invites are -> ', count, ' people.')
