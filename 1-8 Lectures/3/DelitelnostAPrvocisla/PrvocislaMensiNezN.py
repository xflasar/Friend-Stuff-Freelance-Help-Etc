def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def primes_less_than(limit):
    primes_list = []

    for i in range(2, limit):
        if is_prime(i):
            primes_list.append(i)

    return primes_list

# Příklad použití pro vypsání prvočísel menších než 20
result = primes_less_than(15)
print(result)
