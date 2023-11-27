import turtle

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Set the side length of the triangle
triangle_side_length = 100

# Draw the triangle
draw_triangle(triangle_side_length)

# Keep the window open
turtle.done()