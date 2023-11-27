def digit_sum(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    sum_of_digits = 0

    while n > 0:
        digit = n % 10
        sum_of_digits += digit
        n //= 10

    return sum_of_digits

# Příklad použití pro ciferný součet čísla 12345
result = digit_sum(274)
print(result)
