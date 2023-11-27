def draw_h(height):
    if height < 3:
        print("Height must be 3 or greater.")
        return

    middle = height // 2

    for i in range(height):
        if i == middle:
            print("#" * height)
        else:
            print("#" + " " * (height - 2) + "#")

# Příklad použití pro vykreslení písmene "H" o výšce 5
draw_h(3)
