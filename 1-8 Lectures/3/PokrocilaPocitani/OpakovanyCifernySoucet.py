def digit_sum(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    sum_of_digits = 0

    while n > 0:
        digit = n % 10
        sum_of_digits += digit
        n //= 10

    return sum_of_digits

def repeated_digit_sum(n):
    while n >= 10:
        n = digit_sum(n)

    return n

# Příklad použití pro opakovaný ciferný součet čísla 9875
result = repeated_digit_sum(123)
print(result)
