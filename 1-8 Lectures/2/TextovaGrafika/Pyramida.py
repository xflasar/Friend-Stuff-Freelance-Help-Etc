def draw_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        blocks = "#" * (2 * i - 1)
        print(spaces + blocks)

# Příklad použití pro vykreslení pyramidy o velikosti 5
draw_pyramid(5)
