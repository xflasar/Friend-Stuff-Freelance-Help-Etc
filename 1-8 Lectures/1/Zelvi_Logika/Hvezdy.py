import turtle

def draw_star(n, step, side_length):
    angle = step * 360.0 / n
    for i in range(n):
        turtle.forward(side_length)
        turtle.right(angle)

# Nastavte počet vrcholů a délku skoku pro hvězdu
n = 7
step = 3
side_length = 100

# Vykreslení hvězdy
draw_star(n, step, side_length)

# Udržuj okno otevřené
turtle.done()
