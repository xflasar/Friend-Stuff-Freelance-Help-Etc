def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def primes(count):
    if count <= 0:
        raise ValueError("Input must be a positive integer.")

    primes_list = []
    number = 2

    while len(primes_list) < count:
        if is_prime(number):
            primes_list.append(number)
        number += 1

    return primes_list

# Příklad použití pro vypsání prvních 5 prvočísel
result = primes(5)
print(result)
