""" Ask the user to type in their name and then tell them how many vowels
 are in their name """
from faker import Faker
fake = Faker()
name = fake.first_name()

vowels = ['a','e','i','o','u']
vowels_count = 0
for letter in name:
    if letter in vowels:
        vowels_count +=1
print('Your name ', name, 'has ', vowels_count, 'vowels')