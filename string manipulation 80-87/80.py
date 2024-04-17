""" Ask the user to enter their first name and then display
the length of their first name. Then ask for their surname
and display the length of their surname. Join their first
name and surname together with a space between and
display the result. Finally, display the length of their full
name (including the space).  """
from faker import Faker
fake = Faker()

name = fake.first_name()
print(name,'Length of your name is ->', len(name))
last_name = fake.last_name()
print(last_name ,'Length of your last name is ->', len(last_name))
full_name = name+' '+last_name
print(full_name,'Length of your full name is ->', len(full_name))

