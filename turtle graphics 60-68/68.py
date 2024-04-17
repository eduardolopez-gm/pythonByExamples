""" Draw a pattern that will change each time the
program is run. Use the random function to pick
the number of lines, the length of each line and
the angle of each turn.  """

import turtle
import random

lines = random.randint(5,1000)

for i in range(0,lines):
    length = random.randint(20,80)
    rotation = random.randint(1,360)
    turtle.forward(length)
    turtle.right(rotation)
turtle.exitonclick()