#for turtle racing game we are probably going to use setheading, forward, random, and of course an event listener

from turtle import Turtle, Screen 


t = Turtle()

# #Example:
# def move_forwards():
#     t.forward(10)

screen = Screen()

# screen.listen()

# screen.onkey(key= "space", fun=move_forwards)



# end of example

#Assignment - Etch a Sketch App :
# W = Forwards

# S = Backwards

# A = Counter-clockwise (left)

# D = Clockwise (right)

# C = Clear Drawing



def move_forwards():
    t.forward(30)

screen.onkey(key= "W", fun=move_forwards)


def move_backwards():
    t.backward(10)

screen.onkey(key= "S", fun= move_backwards)

def move_counterclockwise():
    t.left(10)

screen.onkey(key= "A", fun= move_counterclockwise)

def move_clockwise():
    t.right(10)

screen.onkey(key= "D", fun= move_clockwise)


def clear():
    t.clear()

screen.onkey(key= "C", fun= clear)












screen.exitonclick()