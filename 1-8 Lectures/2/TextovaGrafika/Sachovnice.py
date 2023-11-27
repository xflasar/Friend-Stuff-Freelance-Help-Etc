def draw_chessboard(n):
    for i in range(n):
        row = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                row += "#"
            else:
                row += "."
        print(row)

# Příklad použití pro vykreslení šachovnice o velikosti 5x5
draw_chessboard(8)
