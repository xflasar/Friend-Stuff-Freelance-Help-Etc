import turtle as t

t.speed(0)

def snowflake(n, length):
  t.penup()
  t.forward(90)
  t.left(45)
  t.pendown()

  def branch():
    for i in range(n):
      # draw V shape
      for i in range(2):
        t.forward(30)
        t.backward(30)
        t.right(90)
      
      # move to next V shape
      t.left(135)
      t.backward(length)
      t.left(45)

    # move to next branch
    t.right(90)
    t.forward(length * n)

  # draw snowflake branches
  for i in range(8):
    branch()
    t.left(45)

  t.exitonclick()

# Test case:
snowflake(5, 10)