import turtle

def draw_polygon(side_length, num_sides):
    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.left(360 / num_sides)

# Set the side length and number of sides for the polygon (e.g., square)
polygon_side_length = 100
polygon_sides = 4  # For a square

# Draw the polygon
draw_polygon(polygon_side_length, polygon_sides)

# Keep the window open
turtle.done()
