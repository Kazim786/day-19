#for turtle racing game we are probably going to use setheading, forward, random, and of course an event listener

from turtle import Turtle, Screen 

import random

t = Turtle()

# #Example:
# def move_forwards():
#     t.forward(10)

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

print(user_bet)

# screen.onkey(key= "space", fun=move_forwards)



# end of example

#Assignment - Etch a Sketch App :

# W = Forwards

# S = Backwards

# A = Counter-clockwise (left)

# D = Clockwise (right)

# C = Clear Drawing



# def move_forwards():
#     t.forward(30)

# screen.onkey("w", move_forwards)


# def move_backwards():
#     t.backward(10)

# screen.onkey(key= "S", fun= move_backwards)

# def move_counterclockwise():
#     t.left(10)

# screen.onkey(key= "A", fun= move_counterclockwise)

# def move_clockwise():
#     t.right(10)

# screen.onkey(key= "D", fun= move_clockwise)


# def clear():
#     t.clear()

# screen.onkey(key= "C", fun= clear)


#Assignment 1 is done


#Assignment 2
#for turtle racing game we are probably going to use speed, forward, random, and of course an event listener

# timmy = Turtle()
# timmy.color("green")
# timmy.shape("turtle")
# timmy.penup()
# timmy.goto(-201, -90)

# timmy.speed(30)

# angelo = Turtle()
# angelo.color("black")
# angelo.shape("turtle")
# angelo.penup()
# angelo.goto(-201, -70)
# angelo.speed(30)

# rambo = Turtle()
# rambo.color("blue")
# rambo.shape("turtle")
# rambo.penup()
# rambo.goto(-201, -50)
# rambo.speed(30)


# lee = Turtle()
# lee.color("yellow")
# lee.shape("turtle")
# lee.penup()
# lee.goto(-201, -30)
# lee.speed(30)

colors = ["red", "green", "orange", "yellow", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
#better way to make turtles
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-201, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
is_race_on = False 

if user_bet:
    is_race_on = True

while is_race_on:
    random_distance = random.randint(0, 10)

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. {winning_color} turtle is the winner")
            else:
                print(f"You lost! {winning_color} turtle is the winner")
    # lee.forward(random_distance)
    # rambo.forward(random_distance)
    # angelo.forward(random_distance)
    # timmy.forward(random_distance)

#after race is over turtles should return back to origin so use lee.home()
















 



screen.exitonclick()