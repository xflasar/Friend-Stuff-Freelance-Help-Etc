def gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative integers.")

    # Funkce pro výpočet největšího společného dělitele dvou čísel
    def find_gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # Kontrola nulových vstupů
    if a == 0 and b == 0:
        raise ValueError("Both numbers cannot be zero.")
    
    # Pokud a nebo b jsou nula, vrátíme druhé nenulové číslo jako výsledek
    if a == 0:
        return abs(b)
    elif b == 0:
        return abs(a)
    
    # Výpočet největšího společného dělitele
    return find_gcd(abs(a), abs(b))

# Příklad použití pro výpočet největšího společného dělitele čísel 48 a 18
result = gcd(5, 7)
print(result)
