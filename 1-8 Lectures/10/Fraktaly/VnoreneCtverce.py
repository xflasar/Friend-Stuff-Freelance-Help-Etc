from turtle import Turtle

julie = Turtle()
julie.speed(10)

def nested_squares(depth: int, length: float = 180.0) -> None:
    if depth == 0:
        return
    else:
        # Draw a square
        for _ in range(4):
            julie.forward(length)
            julie.left(90)
        
        # Move to the starting position of the next square
        julie.penup()
        julie.forward(10)  # Adjust this value for the desired gap between squares
        julie.left(90)
        julie.forward(10)
        julie.right(90)
        julie.pendown()

        # Recursively draw the next square
        nested_squares(depth - 1, length - 20)  # Adjust this value for the desired size reduction

# Set the initial position
julie.penup()
julie.goto(-90, -90)
julie.pendown()

# Call the function to draw nested squares
nested_squares(8)
