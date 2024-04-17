#Draw a five-pointed star. 

import turtle

turtle.begin_fill()
for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()
turtle.exitonclick()