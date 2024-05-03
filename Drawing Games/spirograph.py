import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0 ,255)
    g = random.randint(0 ,255)
    b = random.randint(0 ,255)

    return (r,g,b)



directions = [0, 90, 180, 270 ]

tim.pensize(1)
tim.speed("fastest")


for _ in range(72):
    tim.right(5)
    tim.circle(100)
    tim.color(random_color())
    #tim.pensize(_)

screen = t.Screen()
screen.exitonclick()