# Assignment written by Jillian Hall
# uID: REPLACE_WITH_YOUR_UID
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
# Drawing an elephant in the lower-left empty region
elephant = turtle.Turtle()
elephant.speed("fastest")
elephant.pensize(2)

# Body
elephant.penup()
elephant.goto(-300, -200)
elephant.setheading(0)
elephant.pendown()
elephant.color("dimgray")
elephant.fillcolor("gray")
elephant.begin_fill()
elephant.circle(45)
elephant.end_fill()

# Head
elephant.penup()
elephant.goto(-240, -165)
elephant.pendown()
elephant.color("dimgray")
elephant.fillcolor("darkgray")
elephant.begin_fill()
elephant.circle(30)
elephant.end_fill()

# Ear (behind look — large oval-ish flap)
elephant.penup()
elephant.goto(-255, -130)
elephant.setheading(90)
elephant.pendown()
elephant.color("dimgray")
elephant.fillcolor("slategray")
elephant.begin_fill()
elephant.circle(28, 180)
elephant.left(90)
elephant.forward(56)
elephant.end_fill()

# Inner ear
elephant.penup()
elephant.goto(-250, -125)
elephant.setheading(90)
elephant.pendown()
elephant.color("rosybrown")
elephant.fillcolor("pink")
elephant.begin_fill()
elephant.circle(16, 180)
elephant.left(90)
elephant.forward(32)
elephant.end_fill()

# Trunk — pen travels with lifts between segments for a curve
elephant.penup()
elephant.goto(-210, -145)
elephant.setheading(-20)
elephant.pendown()
elephant.color("dimgray")
elephant.pensize(6)
for _ in range(6):
    elephant.forward(10)
    elephant.right(18)
elephant.pensize(2)

# Eye
elephant.penup()
elephant.goto(-225, -125)
elephant.pendown()
elephant.color("black")
elephant.fillcolor("black")
elephant.begin_fill()
elephant.circle(4)
elephant.end_fill()

# Eye highlight
elephant.penup()
elephant.goto(-224, -123)
elephant.pendown()
elephant.color("white")
elephant.fillcolor("white")
elephant.begin_fill()
elephant.circle(1.5)
elephant.end_fill()

# Tusk
elephant.penup()
elephant.goto(-215, -155)
elephant.setheading(-40)
elephant.pendown()
elephant.color("khaki")
elephant.pensize(3)
elephant.forward(18)
elephant.pensize(2)

# Four legs (pen up between each)
leg_positions = [(-320, -200), (-295, -200), (-275, -200), (-250, -200)]
for x, y in leg_positions:
    elephant.penup()
    elephant.goto(x, y)
    elephant.setheading(270)
    elephant.pendown()
    elephant.color("dimgray")
    elephant.fillcolor("gray")
    elephant.begin_fill()
    elephant.forward(35)
    elephant.left(90)
    elephant.forward(14)
    elephant.left(90)
    elephant.forward(35)
    elephant.left(90)
    elephant.forward(14)
    elephant.end_fill()

# Tail
elephant.penup()
elephant.goto(-340, -155)
elephant.setheading(160)
elephant.pendown()
elephant.color("dimgray")
elephant.pensize(3)
elephant.forward(20)
elephant.right(40)
elephant.forward(10)
elephant.pensize(2)

elephant.hideturtle()

wn.exitonclick()
