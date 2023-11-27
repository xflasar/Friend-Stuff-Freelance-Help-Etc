def vypis_delitele(cislo):
    print(f"Dělitelé čísla {cislo} jsou:")
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            print(i)

# Příklad použití pro vypsání dělitelů čísla 12
vypis_delitele(14)
