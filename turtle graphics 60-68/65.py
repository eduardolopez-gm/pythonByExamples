""" Write the numbers as shown below,
starting at the bottom of the number one.  """
import turtle

#Number 1
turtle.left(90)
turtle.forward(100)

#Move to next number
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()

#Number 2
turtle.forward(75)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)

#Move to next number
turtle.penup()
turtle.forward(50)
turtle.pendown()
#Number 3
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(45)
turtle.left(180)
turtle.forward(45)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)

turtle.hideturtle()

turtle.exitonclick()