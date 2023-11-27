def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

# Příklad použití pro ověření, zda číslo 17 je prvočíslo
result = is_prime(42)
print(result)
