def divisors(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    divisors_list = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors_list.append(i)

    return divisors_list

# Příklad použití pro vypsání dělitelů čísla 12
result = divisors(42)
print(result)
