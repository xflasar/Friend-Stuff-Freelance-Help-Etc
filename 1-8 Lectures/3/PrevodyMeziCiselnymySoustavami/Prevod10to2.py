def convert_10_to_2(n):
    if n == 0:
        return "0"

    binary_result = ""
    while n > 0:
        remainder = n % 2
        binary_result = str(remainder) + binary_result
        n //= 2

    return binary_result

# Příklad použití
decimal_number = 31
binary_representation = convert_10_to_2(decimal_number)
print(f"Binární reprezentace čísla {decimal_number} je: {binary_representation}")
