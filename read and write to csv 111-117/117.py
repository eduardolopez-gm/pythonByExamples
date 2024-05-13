""" Create a simple maths quiz that will ask the user for their name and then generate two
random questions. Store their name, the questions they were asked, their answers and
their final score in a .csv file. Whenever the program is run it should add to the .csv file
and not overwrite anything.  """

import csv
import random
quiz = []
def generate_questions():
    for i in range(0,5):
        number1 = random.randint(10,100)
        number2 = random.randint(10,100)
        quiz.append([number1, number2])
    return quiz


print('--- Welcome to your maths quiz ---')
user_name = input('Enter your name, please: ')


quiz = generate_questions()
file = open('Quiz_score.csv', 'a')


for q in range(0,5):
    score = 0
    question = user_name+"--> "+str(quiz[q][0])+" + "+str(quiz[q][1])+" = "
    print(question)
    user_answer = int(input('Enter your answer: '))
    real_answer = quiz[q][0]+quiz[q][1]
    if user_answer == real_answer:
        score = 1
    
    new_record = question+str(user_answer)+"-"+str(score)+"\n"
    file.write(str(new_record))

file.close()

