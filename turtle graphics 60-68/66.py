""" Draw an octagon that uses a different colour (randomly
selected from a list of six possible colours) for each line.  """
import turtle
import random

turtle.pensize(5)

colors = ['blue','green','red','grey','yellow','orange']

for i in range(0,8):
    turtle.color(random.choice(colors))
    turtle.forward(50)
    turtle.right(45)
turtle.hideturtle()
turtle.exitonclick()


