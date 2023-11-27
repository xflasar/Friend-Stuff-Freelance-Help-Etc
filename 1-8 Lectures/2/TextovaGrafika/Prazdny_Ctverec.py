def draw_filled_square(n):
    for i in range(n):
        for j in range(n):
          if j == 0 or j == n-1 or i == 0 or i == n-1:
            print("#", end=" ")
          else:
            print(".", end=" ")
        print()

# Příklad použití pro vykreslení vyplněného čtverce se stranou 5
draw_filled_square(5)
