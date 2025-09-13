from turtle import Turtle

direction = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

turtle = Turtle()

def dir_reduc(arr):
    for x in arr:
        if x == "NORTH":
            turtle.setheading(90)
        if x == "SOUTH":
            turtle.setheading(270)
        if x == "EAST":
            turtle.setheading(0)
        if x == "NORTH":
            turtle.setheading(180)
    if turtle.heading() == 0:
        return "EAST"
    if turtle.heading() == 90:
        return "NORTH"
    if turtle.heading() == 180:
        return "WEST"
    if turtle.heading() == 270:
        return "SOUTH"

print(dir_reduc(direction))
