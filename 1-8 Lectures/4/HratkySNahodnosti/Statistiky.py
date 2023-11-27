import random

def generate_and_print_stats(lower, upper, count):
    random_numbers = [random.randint(lower, upper) for _ in range(count)]

    # Vypisujeme vygenerovaná čísla
    print("Vygenerovaná čísla:", random_numbers)

    # Vypisujeme nejmenší, největší číslo a aritmetický průměr
    min_number = min(random_numbers)
    max_number = max(random_numbers)
    average = sum(random_numbers) / count

    print(f"Nejmenší číslo: {min_number}")
    print(f"Největší číslo: {max_number}")
    print(f"Aritmetický průměr: {average:.2f}")

# Příklad použití
generate_and_print_stats(1, 100, 10)
