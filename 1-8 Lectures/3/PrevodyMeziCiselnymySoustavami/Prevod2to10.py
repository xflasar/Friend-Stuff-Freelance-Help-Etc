def convert_2_to_10(n):
    decimal_result = 0
    power = 0

    for digit in reversed(n):
        decimal_result += int(digit) * (2 ** power)
        power += 1

    return decimal_result

# Příklad použití
binary_number = "101010"
decimal_representation = convert_2_to_10(binary_number)
print(f"Desítková reprezentace binárního čísla {binary_number} je: {decimal_representation}")
