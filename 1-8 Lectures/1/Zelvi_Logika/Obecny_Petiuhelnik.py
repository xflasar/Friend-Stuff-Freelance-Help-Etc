import turtle

def draw_polygon(side_length, num_sides):
    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.left(360 / num_sides)

# Set the side length and number of sides for the pentagon
pentagon_side_length = 100
pentagon_sides = 5

# Draw the pentagon
draw_polygon(pentagon_side_length, pentagon_sides)

# Keep the window open
turtle.done()
