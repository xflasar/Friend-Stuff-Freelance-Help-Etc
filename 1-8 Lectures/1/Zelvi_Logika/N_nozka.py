import turtle

def draw_square_at_positions(n ,square_side_length):
    turtle.pendown()
    
    # Draw the square at the top-left position
    for _ in range(4):
      turtle.left(-135)
      turtle.forward(square_side_length)
      turtle.left(45)
    
    for _ in range(n):
      turtle.forward(square_side_length)
      turtle.right(45)
      turtle.forward(square_side_length / 2)
      turtle.forward(-(square_side_length / 2))
      turtle.right(90)
      turtle.forward(square_side_length / 2)
      turtle.forward(-(square_side_length / 2))
      turtle.left(135)

draw_square_at_positions(5, 100)

# Keep the window open
turtle.done()
