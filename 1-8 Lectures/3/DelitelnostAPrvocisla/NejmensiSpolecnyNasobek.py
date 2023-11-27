def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be non-zero.")

    abs_a = abs(a)
    abs_b = abs(b)

    # Výpočet nejmenšího společného násobku pomocí vztahu: |a * b| = lcm(a, b) * gcd(a, b)
    return abs_a * abs_b // gcd(abs_a, abs_b)

# Příklad použití pro výpočet nejmenšího společného násobku čísel 12 a 18
result = lcm(6, 9)
print(result)
