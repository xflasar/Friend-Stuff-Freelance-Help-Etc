import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

# Set the side length of the square
square_side_length = 100

# Draw the square
draw_square(square_side_length)

# Keep the window open
turtle.done()
