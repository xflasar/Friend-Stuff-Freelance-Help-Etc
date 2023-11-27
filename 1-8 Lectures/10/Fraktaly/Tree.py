from turtle import Turtle

julie = Turtle()
julie.speed(10)
julie.left(90)

# length: delka kmenove cary
def tree(length: float) -> None:
    if length < 5:  # Base case to stop recursion when the length is small
        return
    else:
        # Draw trunk
        julie.forward(length)

        # Save the current position and heading
        x, y = julie.position()
        heading = julie.heading()

        # Draw first branch
        julie.left(30)
        tree(length * 0.7)

        # Return to saved position and heading
        julie.penup()
        julie.goto(x, y)
        julie.setheading(heading)
        julie.pendown()

        # Draw second branch
        julie.right(60)
        tree(length * 0.7)

        # Return to saved position and heading
        julie.penup()
        julie.goto(x, y)
        julie.setheading(heading)
        julie.pendown()

        # Return to starting position
        julie.right(30)
        julie.backward(length)

# Set the initial position
julie.penup()
julie.goto(0, -200)
julie.pendown()

# Call the function to draw the tree
tree(90)
