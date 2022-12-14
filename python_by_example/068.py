import turtle
import random


lados = random.randint(3,10)
angulo = 180 - ((lados-2)*180)//lados
for i in range(0,10):
    turtle.right(36)
    for i in range(0,lados):
        turtle.forward(50)
        turtle.right(angulo)

turtle.exitonclick()
