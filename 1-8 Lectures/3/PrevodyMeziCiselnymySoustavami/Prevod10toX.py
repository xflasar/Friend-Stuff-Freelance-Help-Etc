def convert_10_to_x(n, symbols):
    if n == 0:
        return symbols[0]

    base = len(symbols)
    result = ""

    while n > 0:
        remainder = n % base
        result = symbols[remainder] + result
        n //= base

    return result

# Příklad použití
decimal_number = 42
symbol_set = "0123456789ABCDEF"  # Pro hexadecimální soustavu
hex_representation = convert_10_to_x(decimal_number, symbol_set)
print(f"Hexadecimální reprezentace čísla {decimal_number} je: {hex_representation}")
