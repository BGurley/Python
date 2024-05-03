from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

is_race_on = False

user_bet = screen.textinput(title = "Bet Selection", prompt="Pick a turtle to win it all! ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winningcolor = turtle.pencolor()
            if winningcolor == user_bet:
                print(f"You've won! The {winningcolor} turtle is the winner!")
            
            else:
                print(f"You've lost! The {winningcolor} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()