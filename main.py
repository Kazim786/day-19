#for turtle racing game we are probably going to use setheading, forward, random, and of course an event listener

from turtle import Turtle, Screen 


t = Turtle()

# #Example:
# def move_forwards():
#     t.forward(10)

screen = Screen()
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
#for turtle racing game we are probably going to use setheading, forward, random, and of course an event listener

timmy = Turtle()
timmy.color("green")
timmy.shape("turtle")
timmy.penup()
timmy.goto(-200, -90)

angelo = Turtle()
angelo.color("black")
angelo.shape("turtle")
angelo.penup()
angelo.goto(-201, -70)

rambo = Turtle()
rambo.color("blue")
rambo.shape("turtle")
rambo.penup()
rambo.goto(-203, -50)



lee = Turtle()
lee.color("yellow")
lee.shape("turtle")
lee.penup()
lee.goto(-204, -30)





















screen.exitonclick()