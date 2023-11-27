def count_letter_a(input_string):
    # Inicializujeme počítadlo na 0
    count = 0

    # Projdeme každý znak v řetězci
    for char in input_string:
        # Porovnáme znak s písmenem A/a
        if char.lower() == 'a':
            # Zvýšíme počítadlo, pokud se jedná o písmeno A/a
            count += 1

    return count

# Příklad použití
text = "This is an example text with several A's and a few a's."
result = count_letter_a(text)

print("Počet výskytů písmene A/a:", result)
