def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def power_factorization(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    factors = []
    divisor = 2

    while n > 1:
        if is_prime(divisor):
            power = 0
            while n % divisor == 0:
                n //= divisor
                power += 1
            if power > 0:
                factors.append((divisor, power))
        divisor += 1

    return factors

# Příklad použití pro mocninný rozklad čísla 72 na prvočísla
result = power_factorization(25)
print(result)
