from math import pi
import turtle

turtle.speed(100)

def arc(r, angle):
  for i in range(angle):
    turtle.forward(2 * pi * r / 360)
    turtle.right(1)

def flower(radius, angle, leaves):
  for i in range(leaves):
    arc(radius, angle)
    turtle.right(180 - angle)
    arc(radius, angle)
    turtle.right(180 - angle + 360.0 / leaves)

flower(100, 80, 9)

turtle.done()