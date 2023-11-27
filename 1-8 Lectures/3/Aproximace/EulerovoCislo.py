from decimal import Decimal, getcontext

def e():
    getcontext().prec = 20  # Nastavte přesnost na šest desetinných míst

    euler_sum = Decimal(0)
    factorial = Decimal(1)

    for n in range(20):  # Nastavte počet iterací podle požadované přesnosti
        euler_sum += Decimal(1) / factorial
        factorial *= Decimal(n + 1)

    return format(euler_sum, '.6f')  # Formátování na šest desetinných míst

# Příklad použití
result = e()
print(result)
