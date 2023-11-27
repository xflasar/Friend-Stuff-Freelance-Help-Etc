def vypis_mocnin(zaklad, n):
    for exponent in range(n):
        vysledek = zaklad ** exponent
        print(f"{zaklad}^{exponent} = {vysledek}")

# Příklad použití pro vypsání prvních 5 mocnin čísla 2
vypis_mocnin(2, 10)
