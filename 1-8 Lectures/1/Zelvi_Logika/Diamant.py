import turtle

def draw_polygon(num_sides, side_length):
    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.left(360 / num_sides)

def draw_diamond(n, side_length):
  for _ in range(n):
    turtle.right(360 / n)
    draw_polygon(n, side_length)
    

# Set the side length of the diamond
diamond_side_length = 100
n = 10

# Draw the diamond
draw_diamond(n, diamond_side_length)

# Keep the window open
turtle.done()
