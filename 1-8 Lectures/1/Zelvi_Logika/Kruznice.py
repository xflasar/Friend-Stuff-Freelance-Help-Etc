import turtle
import math

def draw_circle_by_radius(radius):
    circumference_circle = 2 * math.pi * radius
    num_sides = 100  # Počet stran pro aproximaci kruhu
    side_length = circumference_circle / num_sides

    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.left(360 / num_sides)

# Vykreslí kružnici podle zadaného poloměru
radius = 50

draw_circle_by_radius(radius)

# Udržuj okno otevřené
turtle.done()
