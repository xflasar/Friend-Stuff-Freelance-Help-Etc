def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

# Příklad použití pro výpočet největšího společného dělitele čísel 48 a 18
result = gcd_euclidean(48, 18)
print(result)
