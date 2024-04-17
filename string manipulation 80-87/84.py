""" Ask the user to type in their postcode/city. Display the first
two letters in uppercase.  """
from faker import Faker
fake = Faker()

city = fake.city()
print(city, city[0:3].upper())

