# Assignment written by Jillian Hall
# uID: U1503415
#
# Assignment 2 - Turtle Graphics

import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Assignment 2 - Turtle Graphics")
wn.setup(width=800, height=600)

# a) Draw a triangle
# Make a turtle named triangle. The triangle must start and end at (0, 0).
triangle = turtle.Turtle()
triangle.speed("fastest")
triangle.color("red")
triangle.pensize(3)
triangle.penup()
triangle.goto(0, 0)
triangle.setheading(60)
triangle.pendown()
for _ in range(3):
    triangle.forward(120)
    triangle.right(120)
triangle.hideturtle()

# b) Draw a zig-zag
# Make a turtle named zigzag. Blue. Start (-100, 100). Loop with 8 peaks.
zigzag = turtle.Turtle()
zigzag.speed("fastest")
zigzag.color("blue")
zigzag.pensize(2)
zigzag.penup()
zigzag.goto(-100, 100)
zigzag.setheading(60)
zigzag.pendown()
for i in range(8):
    zigzag.forward(35)
    zigzag.right(120)
    zigzag.forward(35)
    zigzag.left(120)
zigzag.hideturtle()

# c) Draw a square green spiral
# Make a turtle named spiral. Green. Start (0, -100). Loop with growing length.
spiral = turtle.Turtle()
spiral.speed("fastest")
spiral.color("green")
spiral.pensize(2)
spiral.penup()
spiral.goto(0, -100)
spiral.setheading(0)
spiral.pendown()
for i in range(1, 25):
    spiral.forward(i * 4)
    spiral.left(90)
spiral.hideturtle()

# d) Your own picture
# Drawing a simple house with a sun in the lower-left empty region
house = turtle.Turtle()
house.speed("fastest")
house.pensize(2)

# Sun
house.penup()
house.goto(-280, -20)
house.pendown()
house.color("orange")
house.fillcolor("yellow")
house.begin_fill()
house.circle(25)
house.end_fill()
# Sun rays
house.color("orange")
for angle in range(0, 360, 45):
    house.penup()
    house.goto(-280, 5)
    house.setheading(angle)
    house.forward(30)
    house.pendown()
    house.forward(15)

# House body
house.penup()
house.goto(-320, -200)
house.setheading(0)
house.pendown()
house.color("brown")
house.fillcolor("tan")
house.begin_fill()
for _ in range(4):
    house.forward(100)
    house.left(90)
house.end_fill()

# Roof
house.penup()
house.goto(-320, -100)
house.pendown()
house.color("darkred")
house.fillcolor("red")
house.begin_fill()
house.goto(-270, -40)
house.goto(-220, -100)
house.goto(-320, -100)
house.end_fill()

# Door
house.penup()
house.goto(-285, -200)
house.setheading(0)
house.pendown()
house.color("saddlebrown")
house.fillcolor("sienna")
house.begin_fill()
house.forward(30)
house.left(90)
house.forward(45)
house.left(90)
house.forward(30)
house.left(90)
house.forward(45)
house.end_fill()

# Window
house.penup()
house.goto(-255, -145)
house.setheading(0)
house.pendown()
house.color("navy")
house.fillcolor("skyblue")
house.begin_fill()
for _ in range(4):
    house.forward(28)
    house.left(90)
house.end_fill()
# Window panes
house.penup()
house.goto(-255, -131)
house.pendown()
house.goto(-227, -131)
house.penup()
house.goto(-241, -145)
house.pendown()
house.goto(-241, -117)

house.hideturtle()

wn.exitonclick()
