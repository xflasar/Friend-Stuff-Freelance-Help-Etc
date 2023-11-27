def factorial(n):
    result = 1
    i = 1

    while i <= n:
        result *= i
        i += 1

    return result

# Příklad použití pro výpočet faktoriálu čísla 5
result = factorial(10)
print(result)
