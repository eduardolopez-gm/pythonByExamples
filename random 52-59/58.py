""" Make a maths quiz that asks five questions by randomly
generating two whole numbers to make the question
(e.g. [num1] + [num2]). Ask the user to enter the
answer. If they get it right add a point to their score. At
the end of the quiz, tell them how many they got correct
out of five.  """

import random
correct_answers = 0
print('Welcome to the maths quiz')
print('You will ask to solve 5 questions')
for question in range(0,5):
    random_number1 = random.randint(1,100)
    random_number2 = random.randint(1,100)
    result = random_number1 + random_number2
    print('Please give an answer to ', random_number1, '+', random_number2)
    user_answer = int(input())
    if result == user_answer:
        correct_answers +=1
print('Quiz finished')
print('You answered ', correct_answers, ' questions correctly')
