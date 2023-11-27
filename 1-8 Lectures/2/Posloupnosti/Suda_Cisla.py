def vypis_suda_cisla(n):
    cislo = 2  # Začínáme s prvním sudým číslem
    while n > 0:
        print(cislo)
        cislo += 2  # Přejdeme na další sudé číslo
        n -= 1

# Příklad použití pro vypsání prvních 5 sudých čísel
vypis_suda_cisla(10)