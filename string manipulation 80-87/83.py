""" Ask the user to type in a word in upper case. If they
type it in lower case, ask them to try again. Keep
repeating this until they type in a message all in uppercase.  """
from faker import Faker
fake = Faker()

word = fake.word()

while word.islower():
    print(word)
    # create new data
    word = fake.word()
    random_choice = fake.random_int(0,9)
    # end condition
    if random_choice == 8:
        word = word.upper()
print(word)
    

