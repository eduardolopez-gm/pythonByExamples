""" Change program 076 so that once the user has completed their list of names, display the
full list and ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they
answer “no”, delete that entry from the list and display the list again.  """
import random
# pip install faker, uses to create random data
from faker import Faker
fake = Faker()

# Add 3 people to the list
invites_list = []
for i in range(0,3):
    invites_list.append(fake.first_name())

# Iterate to add more people to the list
end_condition = ''
while end_condition != 0:
    invites_list.append(fake.first_name())
    end_condition = random.randint(0,1)


print(invites_list)
print('You have invited',len(invites_list), 'people to the party')

user_answer = input('Enter a name from the list:  ')
if user_answer in invites_list:
    print('Do you want ', user_answer,' come to the party? (yes/no)  :')
    invite_confirmation = input()
    if invite_confirmation == 'no':
        del invites_list[invites_list.index(user_answer)]

print('Final list ', invites_list)