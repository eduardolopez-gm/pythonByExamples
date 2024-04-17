""" Draw three squares in a row with a gap
between each. Fill them using three different colours.  """

import turtle
colors = ['red', 'green', 'blue']

for square in range(0,3):
    turtle.color('black', colors[square])
    turtle.begin_fill()
    for side in range(0,4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(120)
    turtle.pendown()
turtle.exitonclick()