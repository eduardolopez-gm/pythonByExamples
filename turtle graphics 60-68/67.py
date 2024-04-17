""" Create the following pattern:  """

import turtle

turtle.pensize(2)
for shape in range(0,10):
    for side in range(0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()
turtle.exitonclick()