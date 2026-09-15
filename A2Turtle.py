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
# Drawing a ski mountain scene (peaks, snow, trees, and a lift)
mountain = turtle.Turtle()
mountain.speed("fastest")
mountain.pensize(2)

# Back mountain peak
mountain.penup()
mountain.goto(-360, -220)
mountain.pendown()
mountain.color("steelblue", "slategray")
mountain.begin_fill()
mountain.goto(-280, -40)
mountain.goto(-200, -220)
mountain.goto(-360, -220)
mountain.end_fill()

# Front mountain peak (taller)
mountain.penup()
mountain.goto(-320, -220)
mountain.pendown()
mountain.color("dimgray", "gray")
mountain.begin_fill()
mountain.goto(-250, -10)
mountain.goto(-150, -220)
mountain.goto(-320, -220)
mountain.end_fill()

# Snow cap on front peak
mountain.penup()
mountain.goto(-278, -70)
mountain.pendown()
mountain.color("lightgray", "white")
mountain.begin_fill()
mountain.goto(-250, -10)
mountain.goto(-215, -70)
mountain.goto(-278, -70)
mountain.end_fill()

# Snow cap on back peak
mountain.penup()
mountain.goto(-310, -90)
mountain.pendown()
mountain.color("lightgray", "white")
mountain.begin_fill()
mountain.goto(-280, -40)
mountain.goto(-250, -90)
mountain.goto(-310, -90)
mountain.end_fill()

# Ski lift cable
mountain.penup()
mountain.goto(-330, -200)
mountain.pendown()
mountain.color("black")
mountain.pensize(1)
mountain.goto(-260, -30)
mountain.pensize(2)

# Lift towers — pen up between each
for tx, ty, th in [(-320, -220, 45), (-290, -150, 40), (-265, -70, 35)]:
    mountain.penup()
    mountain.goto(tx, ty)
    mountain.setheading(90)
    mountain.pendown()
    mountain.color("saddlebrown")
    mountain.pensize(3)
    mountain.forward(th)
    # Crossbar
    mountain.left(90)
    mountain.forward(8)
    mountain.backward(16)
    mountain.forward(8)
    mountain.right(90)
    mountain.pensize(2)

# Chair on the cable
mountain.penup()
mountain.goto(-295, -120)
mountain.pendown()
mountain.color("red", "tomato")
mountain.begin_fill()
mountain.setheading(0)
for _ in range(2):
    mountain.forward(14)
    mountain.right(90)
    mountain.forward(10)
    mountain.right(90)
mountain.end_fill()
# Hanger from cable
mountain.penup()
mountain.goto(-288, -110)
mountain.pendown()
mountain.color("black")
mountain.setheading(270)
mountain.forward(10)

# Pine trees at the base — pen up between trees
tree_spots = [(-350, -220), (-335, -220), (-175, -220), (-160, -220), (-145, -220)]
for tx, ty in tree_spots:
    # Trunk
    mountain.penup()
    mountain.goto(tx, ty)
    mountain.setheading(90)
    mountain.pendown()
    mountain.color("saddlebrown", "sienna")
    mountain.begin_fill()
    mountain.forward(12)
    mountain.right(90)
    mountain.forward(6)
    mountain.right(90)
    mountain.forward(12)
    mountain.right(90)
    mountain.forward(6)
    mountain.end_fill()
    # Needles (stacked triangles)
    mountain.color("darkgreen", "forestgreen")
    for level, size in enumerate((18, 14, 10)):
        mountain.penup()
        mountain.goto(tx - size / 2 + 3, ty + 10 + level * 10)
        mountain.setheading(0)
        mountain.pendown()
        mountain.begin_fill()
        mountain.goto(tx + 3, ty + 28 + level * 10)
        mountain.goto(tx + size / 2 + 3, ty + 10 + level * 10)
        mountain.goto(tx - size / 2 + 3, ty + 10 + level * 10)
        mountain.end_fill()

# Sun in the upper-left of the scene
mountain.penup()
mountain.goto(-355, -5)
mountain.pendown()
mountain.color("orange", "yellow")
mountain.begin_fill()
mountain.circle(16)
mountain.end_fill()

mountain.hideturtle()

wn.exitonclick()
