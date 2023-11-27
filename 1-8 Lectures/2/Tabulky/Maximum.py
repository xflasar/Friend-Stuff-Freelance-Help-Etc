def table_products(n):
    # Vytvoření tabulky
    table = [[0] * (n + 1) for _ in range(n + 1)]

    # Naplnění tabulky součiny čísel řádku a sloupce
    for i in range(1, n + 1):
        for j in range(1, n + 1):
          if i > j:
            table[i][j] = i
          else:
            table[i][j] = j

    # Vypsání tabulky
    print("    " + " ".join(map(str, range(1, n + 1))))
    print("    " + " -" * n * 2)
    for i in range(1, n + 1):
        print(f"{i} |", " ".join(map(str, table[i][1:])))

# Příklad použití pro vypsání tabulky 5x5
table_products(5)
