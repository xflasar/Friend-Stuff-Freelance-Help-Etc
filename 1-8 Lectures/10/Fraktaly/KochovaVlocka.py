from turtle import Turtle

julie = Turtle()
julie.speed(10)
julie.penup()
julie.setposition(-190, 0)
julie.pendown()

# depth: pocet rekurzivnich zanoreni
# size: sirka krivky
def koch(depth: int = 5, size: float = 380.0) -> None:
    if depth == 0:
        julie.forward(size)
    else:
        koch(depth - 1, size / 3)
        julie.left(60)
        koch(depth - 1, size / 3)
        julie.right(120)
        koch(depth - 1, size / 3)
        julie.left(60)
        koch(depth - 1, size / 3)

# Call the function to draw the Koch curve
koch(5)
