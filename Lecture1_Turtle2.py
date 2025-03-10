import turtle
import random

# Create the turtle and screen objects
Turtle = turtle.Turtle()
Window = turtle.Screen()
Window.bgcolor("black")  # Set background color
Turtle.speed(0)  # Max speed for smooth drawing
Turtle.width(2)  # Set the line thickness
Turtle.hideturtle()

# List of colors for the symmetry
colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta"]

# Function to draw a single symmetric pattern
def draw_symmetric_pattern(myTurtle, linelen, repetitions):
    angle = 360 / repetitions
    for _ in range(repetitions):
        myTurtle.color(random.choice(colors))
        myTurtle.forward(linelen)
        myTurtle.circle(linelen / 4)
        myTurtle.backward(linelen)
        myTurtle.right(angle)

# Function to layer multiple symmetric patterns
def draw_complex_symmetry(myTurtle, layers, initial_length):
    for i in range(layers):
        draw_symmetric_pattern(myTurtle, initial_length, 12)
        initial_length -= 20  # Reduce size for the next layer
        myTurtle.penup()
        myTurtle.goto(0, -i * 10)  # Center each layer
        myTurtle.pendown()

# Draw the complex symmetric pattern
draw_complex_symmetry(Turtle, 10, 200)

# Close the window on click
Window.exitonclick()
