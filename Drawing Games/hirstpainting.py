import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")



color_list = [(238, 230, 217), (235, 148, 72), (214, 230, 239), (241, 225, 234), (228, 241, 235), (29, 112, 162), (107, 175, 208), (164, 10, 37), (186, 173, 14), (162, 52, 93), (234, 83, 43), (28, 131, 69), (12, 171, 210), (183, 74, 36), (61, 15, 31), (44, 24, 15), (225, 204, 104), (19, 29, 67), (206, 63, 116), (3, 111, 82), (118, 182, 150), (200, 136, 170), (10, 47, 32), (61, 166, 103), (134, 215, 229), (20, 52, 128), (109, 113, 177), (237, 163, 194), (169, 18, 12), (243, 199, 2)]

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.fd(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)
        
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = tim.Screen()
screen.exitonclick()
