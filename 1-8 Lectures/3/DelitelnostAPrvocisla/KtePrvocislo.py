def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def kth_prime(k):
    if k <= 0:
        raise ValueError("Input must be a positive integer.")

    count = 0
    number = 2

    while count < k:
        if is_prime(number):
            count += 1
        number += 1

    return number - 1

# Příklad použití pro získání 5. prvočísla
result = kth_prime(10)
print(result)
