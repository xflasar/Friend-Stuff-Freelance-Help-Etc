import turtle

def spiral(n, angle, step):
  for i in range(n):
    turtle.forward(step * i)
    turtle.right(angle)

spiral(100, 61, 1)

turtle.done()