""" Show the user a line of text from your favourite poem
and ask for a starting and ending point. Display the
characters between those two points.  """
from faker import Faker
fake = Faker()

poem = fake.paragraph()
print(poem)

# Create random index to slice the poem
start_index = fake.random_int(0, len(poem)//2)
end_index = fake.random_int(len(poem)//2,len(poem))
print('Indexes', start_index, end_index)

# Sliced poem based on index
print(poem[start_index:end_index])

