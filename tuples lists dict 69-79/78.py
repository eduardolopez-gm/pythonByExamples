""" Create a list containing the titles of four TV programmes and display
them on separate lines. Ask the user to enter another show and a
position they want it inserted into the list. Display the list again,
showing all five TV programmes in their new positions.  """
from faker import Faker
fake = Faker()

tv_shows = []
for i in range(0,5):
    tv_shows.append(fake.text(max_nb_chars=30))
    print(tv_shows[i])
# Generate random data
random_tv_show = fake.text(max_nb_chars=30)
random_tv_show_index = fake.random_int(0,5)
print('Random tv show name generated ->',random_tv_show)
print('Random index generated ->',random_tv_show_index)
tv_shows.insert(random_tv_show_index,random_tv_show)                         

for i in range(0,len(tv_shows)):
    print(tv_shows[i])
