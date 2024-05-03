from turtle import Turtle, Screen
import random

tim = Turtle()
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

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range (3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

    














screen = Screen()
screen.exitonclick()