""" Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).  """

nursery_rhyme = ['This Little Piggy Went to Market', 'Round and Round the Garden',  'Jack in the Box']

for rhyme in nursery_rhyme:
    print('Original rhyme -> ',rhyme)
    print('Length of the rhyme ->',len(rhyme))
    print('Slice rhyme from position 3 to 12 ->',rhyme[3:12], '\n')
