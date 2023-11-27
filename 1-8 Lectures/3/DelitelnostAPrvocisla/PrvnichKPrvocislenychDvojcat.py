def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def twin_primes(count):
    if count <= 0:
        raise ValueError("Input must be a positive integer.")

    twin_primes_list = []
    number = 3  # Start from the first twin prime pair (3, 5)

    while len(twin_primes_list) < count:
        if is_prime(number) and is_prime(number + 2):
            twin_primes_list.append((number, number + 2))
        number += 2  # Skip even numbers as they are not prime

    return twin_primes_list

# Příklad použití pro vypsání prvních 5 prvočíselných dvojčat
result = twin_primes(5)
print(result)
