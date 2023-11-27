def product_without_zeros(numbers):
    # Inicializace součinu na 1
    product = 1
    
    # Iterace přes čísla v seznamu
    for number in numbers:
        # Pokud číslo není nula, přidáme ho k součinu
        if number != 0:
            product *= number
    
    return product

# Příklad použití
my_numbers = [2, 3, 0, 5, 7, 0, 4]
result = product_without_zeros(my_numbers)
print("Součin bez nul:", result)
