""" Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again.  """

subjects = ['Maths', 'Literacy', 'Physics', 'Chemistry', 'Programming' , 'Web Design']
print('Original list -> ', subjects)
user_choice = input('Enter the subject that you dont like from the list :')
del subjects[subjects.index(user_choice)]
print('Modified list -> ', subjects)