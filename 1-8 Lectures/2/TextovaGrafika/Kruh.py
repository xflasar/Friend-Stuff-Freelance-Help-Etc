import math

def draw_circle(r):
    for y in range(-r, r + 1):
        row = ""
        for x in range(-r, r + 1):
            distance = math.sqrt(x**2 + y**2)
            if distance < r:
                row += "#"
            else:
                row += "."
        print(row)

# Example usage to draw a circle with radius 5
draw_circle(5)
