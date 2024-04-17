""" Create an empty list called “nums”. Ask the user to enter numbers.
After each number is entered, add it to the end of the nums list and
display the list. Once they have entered three numbers, ask them if
they still want the last number they entered saved. If they say “no”,
remove the last item from the list. Display the list of numbers.  """
from faker import Faker
fake = Faker()

nums = []
end_condition = ''
# Create random numbers to add to the list
while end_condition != 0:
    nums.append(fake.random_int(1,999))
    print(nums)
    end_condition = fake.random_int(0,1)

del nums[len(nums)-1]
print(nums)


