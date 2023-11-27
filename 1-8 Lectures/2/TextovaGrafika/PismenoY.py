def draw_y(height):
    if height < 3:
        print("Height must be 3 or greater.")
        return

    middle = height // 2

    for i in range(height):
        if i < middle:
            row = " " * i + "#" + " " * (2 * (middle - i) - 1) + "#"
        else:
            row = " " * middle + "#" + " " * (height - middle - 1)
        print(row)

# Příklad použití pro vykreslení písmene "Y" o výšce 5
draw_y(5)
