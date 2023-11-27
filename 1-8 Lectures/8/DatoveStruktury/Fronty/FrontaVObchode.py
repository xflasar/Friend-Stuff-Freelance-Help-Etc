def queue_time(customers, n):
    if not customers:
        return 0

    if n <= 0:
        raise ValueError("Počet pokladen musí být větší než 0.")

    pokladny = [0] * n  # Inicializace pokladen s časy 0

    for time in customers:
        min_pokladna = min(pokladny)
        index_min_pokladna = pokladny.index(min_pokladna)
        pokladny[index_min_pokladna] += time

    return max(pokladny)

# Příklad použití:
customers = [2, 5, 3, 4, 6]
pokladny = 2
vysledek = queue_time(customers, pokladny)
print(f"Nejmenší možný celkový čas: {vysledek}")
