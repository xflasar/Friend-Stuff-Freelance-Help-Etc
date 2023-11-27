def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def factorization(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    factors = []
    divisor = 2

    while n > 1:
        if is_prime(divisor) and n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors

# Příklad použití pro rozklad čísla 84 na prvočísla
result = factorization(42)
print(result)
