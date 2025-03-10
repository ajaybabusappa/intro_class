import turtle
import colorsys

def draw_hypnotic_circles():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Hypnotic Circles")

    hypnotic = turtle.Turtle()
    hypnotic.speed("fastest")  # Set the speed to the fastest
    hypnotic.hideturtle()

    screen.tracer(2)

    num_circles = 36  # Number of circles in each layer
    num_layers = 10  # Number of layers of circles
    radius_increment = 10  # Increase in radius for each layer

    # Generate colors dynamically using the HSV color model
    for layer in range(num_layers):
        radius = (layer + 1) * radius_increment
        for i in range(num_circles):
            hue = i / num_circles
            r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
            hypnotic.color(r, g, b)
            hypnotic.penup()
            hypnotic.goto(0, -radius)
            hypnotic.pendown()
            hypnotic.circle(radius)
            hypnotic.right(360 / num_circles)

    screen.mainloop()

draw_hypnotic_circles()