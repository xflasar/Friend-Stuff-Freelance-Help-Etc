def divisors_count(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    divisors_count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            divisors_count += 1

    return divisors_count

# Příklad použití pro získání počtu dělitelů čísla 12
result = divisors_count(42)
print(result)