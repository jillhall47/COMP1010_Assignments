# A2 Turtle Assignment
# Starter code by David Johnson
# For COMP1010 University of Utah
# Assignment written by Jillian Hall
# uID: U1503415

# Use the turtle module
import turtle

# Create a screen to draw on
window = turtle.Screen()
window.bgcolor("white")

# A2 a)
# Make a turtle named triangle and use that turtle to draw
# a triangle with one corner at position x = 0 and y = 0
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

# A2 b)
# Make a turtle named zigzag and use that turtle to draw
# a blue zigzag shape starting at position x = -100 and y = 100.
# See the assignment for an example picture. You must use a
# loop to repeat the pattern for 8 peaks.
# The turtle should not leave any other lines except the zig zag.
zigzag = turtle.Turtle()
zigzag.speed("fastest")
zigzag.color("blue")
zigzag.pensize(2)
zigzag.penup()
zigzag.goto(-100, 100)
zigzag.pendown()
for i in range(8):
    zigzag.left(60)
    zigzag.forward(40)
    zigzag.right(120)
    zigzag.forward(40)
    zigzag.left(60)
zigzag.hideturtle()

# A2 c)
# Make a turtle named spiral and use that turtle to draw
# a green square spiral starting at position x = 0 and y = -100.
# You must use a loop to form the spiral. As a hint, the length of
# each part of the spiral gets longer. Use the loop counter variable
# and some math to make a growing length as the loop repeats.
spiral = turtle.Turtle()
spiral.speed("fastest")
spiral.color("green")
spiral.pensize(2)
spiral.penup()
spiral.goto(0, -100)
spiral.pendown()
for i in range(25):
    spiral.forward((i + 1) * 5)
    spiral.left(90)
spiral.hideturtle()

# A2 d)
# Add a new turtle. Draw a nice picture of your own design.
# There should be different colors and sections that require
# the turtle pen to go up and then back down to draw it.
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

# Keep window open when run locally; skip on autograder mocks
if hasattr(window, "exitonclick"):
    window.exitonclick()
