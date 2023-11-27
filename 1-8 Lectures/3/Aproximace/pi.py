from decimal import Decimal, getcontext

def pi():
    getcontext().prec = 100  # Nastavte přesnost na dostatečně vysokou hodnotu

    pi_approximation = Decimal(0)
    sign = 1

    for n in range(1000):  # Nastavte počet iterací podle požadované přesnosti
        term = Decimal(sign) / Decimal(2 * n + 1)
        pi_approximation += term
        sign *= -1

    return format(pi_approximation * Decimal(4), '.3f')  # Formátování na tisíciny

# Příklad použití
result = pi()
print(result)
