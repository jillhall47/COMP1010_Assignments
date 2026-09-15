# Assignment written by Jillian Hall
# uID: REPLACE_WITH_YOUR_UID
#
# Assignment 2 - Turtle Graphics

import turtle
import math

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
# Drawing a side-view elephant in the lower-left empty region
elephant = turtle.Turtle()
elephant.speed("fastest")
elephant.pensize(2)


def filled_ellipse(t, cx, cy, rx, ry, outline, fill):
    """Draw a filled ellipse centered at (cx, cy)."""
    t.penup()
    t.goto(cx + rx, cy)
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    for deg in range(0, 361, 2):
        rad = math.radians(deg)
        t.goto(cx + rx * math.cos(rad), cy + ry * math.sin(rad))
    t.end_fill()


# Legs first (drawn under the body) — pen up between each leg
leg_data = [
    (-330, -195, 16, 48),  # back left
    (-305, -195, 16, 48),  # back right
    (-255, -195, 16, 48),  # front left
    (-230, -195, 16, 48),  # front right
]
for lx, ly, lw, lh in leg_data:
    elephant.penup()
    elephant.goto(lx, ly)
    elephant.setheading(0)
    elephant.pendown()
    elephant.color("dimgray", "gray")
    elephant.begin_fill()
    for _ in range(2):
        elephant.forward(lw)
        elephant.right(90)
        elephant.forward(lh)
        elephant.right(90)
    elephant.end_fill()
    # Foot pad
    elephant.penup()
    elephant.goto(lx + lw / 2, ly - lh)
    elephant.pendown()
    elephant.color("dimgray", "slategray")
    elephant.begin_fill()
    elephant.setheading(0)
    elephant.circle(7)
    elephant.end_fill()

# Body (horizontal oval)
filled_ellipse(elephant, -280, -145, 70, 48, "dimgray", "gray")

# Big ear (behind the head)
filled_ellipse(elephant, -255, -115, 38, 48, "dimgray", "darkgray")
# Inner ear
filled_ellipse(elephant, -250, -115, 22, 30, "rosybrown", "lightpink")

# Head
filled_ellipse(elephant, -215, -130, 36, 34, "dimgray", "darkgray")

# Trunk — thick filled curve curling under
elephant.penup()
elephant.goto(-185, -145)
elephant.pendown()
elephant.color("dimgray", "gray")
elephant.pensize(1)
elephant.begin_fill()
elephant.setheading(-55)
# Outer edge of trunk
for i in range(14):
    elephant.forward(7)
    elephant.right(9)
# Tip and back up the inner edge
elephant.left(90)
elephant.forward(14)
elephant.left(90)
for i in range(14):
    elephant.forward(6)
    elephant.left(9)
elephant.end_fill()
elephant.pensize(2)

# Tusks (cream colored) — pen up between them
for heading, start in ((-50, (-195, -150)), (-70, (-200, -155))):
    elephant.penup()
    elephant.goto(start)
    elephant.setheading(heading)
    elephant.pendown()
    elephant.color("khaki", "ivory")
    elephant.begin_fill()
    elephant.pensize(1)
    elephant.forward(22)
    elephant.right(25)
    elephant.forward(6)
    elephant.right(140)
    elephant.forward(26)
    elephant.end_fill()
    elephant.pensize(2)

# Eye
elephant.penup()
elephant.goto(-205, -118)
elephant.pendown()
elephant.color("black", "white")
elephant.begin_fill()
elephant.circle(6)
elephant.end_fill()
elephant.penup()
elephant.goto(-203, -116)
elephant.pendown()
elephant.color("black", "black")
elephant.begin_fill()
elephant.circle(3)
elephant.end_fill()

# Tail with tuft — pen up to start, then draw
elephant.penup()
elephant.goto(-348, -140)
elephant.setheading(200)
elephant.pendown()
elephant.color("dimgray")
elephant.pensize(3)
elephant.forward(22)
elephant.right(25)
elephant.forward(12)
# Tuft
elephant.pensize(2)
for angle in (-40, 0, 40):
    elephant.penup()
    elephant.forward(0)
    tip = elephant.position()
    heading = elephant.heading()
    elephant.setheading(heading + angle)
    elephant.pendown()
    elephant.forward(10)
    elephant.penup()
    elephant.goto(tip)
    elephant.setheading(heading)

elephant.hideturtle()

wn.exitonclick()
