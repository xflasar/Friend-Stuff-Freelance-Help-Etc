def draw_n(height):
    if height < 3:
        print("Height must be 3 or greater.")
        return

    for i in range(height):
        row = "#" + " " * (i) + "#" + " " * (height - i - 1) + "#"
        print(row)

# Příklad použití pro vykreslení písmene "N" o výšce 5
draw_n(5)
