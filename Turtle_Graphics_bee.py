import turtle

"""
  A bit of a hacky solution, but it works.
  The idea is to draw a honeycomb of a given length (which by my understanding is circles from center comb).
  The comb is made up of 6 sides (hexagon).
"""

def honeycomb(length):
  size = 20 # Optional size of the comb
  turtle.speed(0)

  # function for moving the turtle
  def move(sideLength, sideAngle):
    turtle.right(sideAngle)
    turtle.forward(sideLength)

  # function for drawing a comb
  def comb():
    turtle.pendown()
    for i in range(6):
            move(size,-60)
    turtle.penup()

  # start
  turtle.penup()

  for combCircle in range (length):
    if combCircle == 0:
            comb()
            move(size,-60)
            move(size,-60)
            move(size,-60)
            move(0,180)
    for i in range (6):
            move(0,60)
            for j in range (combCircle+1):
                    comb()
                    move(size,-60)
                    move(size,60)
            move(-size,0)
    move(-size,60)
    move(size,-120)
    move(0,60)

  turtle.exitonclick()

# Test case:
honeycomb(1)