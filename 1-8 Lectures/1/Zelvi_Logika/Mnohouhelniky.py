import turtle

def draw_polygon(num_sides, side_length):
    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.left(360 / num_sides)

# Set the number of sides and side length for the polygon
num_sides = 6  # Change this to the desired number of sides
side_length = 100

# Draw the polygon
draw_polygon(num_sides, side_length)

# Keep the window open
turtle.done()
