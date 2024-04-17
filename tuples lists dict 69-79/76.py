""" Ask the user to enter the names of three people they want to
invite to a party and store them in a list. After they have entered
all three names, ask them if they want to add another. If they do,
allow them to add more names until they answer “no”. When
they answer “no”, display how many people they have invited to
the party. """
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


#print(fake.first_name())