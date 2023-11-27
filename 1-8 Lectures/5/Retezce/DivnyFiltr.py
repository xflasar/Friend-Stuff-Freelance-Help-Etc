def filter_text(s):
    # Ignorujeme diakritiku a převedeme na velká písmena
    s = s.upper()

    # Převedeme text na seznam písmen
    letters = list(s)

    # Inicializujeme indexy pro poslední dvě písmena
    prev_prev_index = 0
    prev_index = 1  # Nyní začínáme od druhého písmena, abychom měli co sčítat

    # Projdeme seznam písmen
    while prev_index < len(letters) - 1:  # Opraveno, abychom se vyhnuli indexování mimo rozsah
        # Spočteme hodnoty dvou předchozích písmen
        prev_prev_value = ord(letters[prev_prev_index]) - ord('A') + 1
        prev_value = ord(letters[prev_index]) - ord('A') + 1

        # Pokud součet hodnot dvou předchozích písmen odpovídá hodnotě aktuálního písmene
        if prev_prev_value + prev_value == ord(letters[prev_index + 1]) - ord('A') + 1:
            # Odstraníme aktuální písmeno
            del letters[prev_index + 1]
        else:
            # Posuneme indexy pro další iteraci
            prev_prev_index = prev_index
            prev_index += 1

    # Spočteme novou hodnotu pro případ, že bychom mazali poslední písmeno
    new_value = ord(letters[-2]) - ord('A') + 1 + ord(letters[-1]) - ord('A') + 1

    # Pokud součet hodnot dvou posledních písmen odpovídá hodnotě prvního písmena
    if new_value == ord(letters[0]) - ord('A') + 1:
        # Odstraníme první písmeno
        del letters[0]

    # Spočteme výsledný řetězec
    result = ''.join(letters)

    return result

# Příklad použití
input_text = "ABCDEF"
filtered_text = filter_text(input_text)

print(f"Vstupní text: {input_text}")
print(f"Filtrovaný text: {filtered_text}")
