""" Ask the user to type in their favourite school subject.
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-. """
from faker import Faker
fake = Faker()

subject = fake.word()
subject = subject.title()
for letter in subject:
    print(letter, end='-')


