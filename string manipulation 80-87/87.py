""" Ask the user to type in a word and then display it backwards on separate lines. For
instance, if they type in “Hello” it should display as shown below: 
--> hello 
o
l
l
e
h """

from faker import Faker
fake = Faker()

word = fake.word()
print(word)
for letter in range(len(word)-1,-1,-1):
    print(word[letter])
