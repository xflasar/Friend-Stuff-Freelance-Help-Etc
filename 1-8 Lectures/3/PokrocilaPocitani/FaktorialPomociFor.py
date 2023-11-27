def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

# Příklad použití pro výpočet faktoriálu čísla 5
result = factorial(50)
print(result)
