import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# timmytheturtle.shape("turtle")
# timmytheturtle.color("green")
# timmytheturtle.forward(100)
# timmytheturtle.right(90)
# timmytheturtle.forward(100)
# timmytheturtle.right(90)
# timmytheturtle.forward(100)
# timmytheturtle.right(90)
# timmytheturtle.forward(100)
# timmytheturtle.right(90)
def random_color():
    r = random.randint(0 ,255)
    g = random.randint(0 ,255)
    b = random.randint(0 ,255)

    return (r,g,b)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270 ]
tim.pensize(15)
tim.speed("fastest")


for _ in range(200):
    tim.forward(30)
    tim.right(random.choice(directions))
    tim.color(random_color())
    #tim.pensize(_)





