import random

def simulate_test_probability(n, count):
    successful_attempts = 0

    for _ in range(count):
        # Simulace testu
        correct_answers = 0
        for _ in range(n):
            # Náhodně vyber jednu možnost (1 až 4, představující odpovědi A, B, C, D)
            chosen_option = random.randint(1, 4)

            # Pokud je vybraná možnost 1 (správná odpověď), inkrementuj počet správných odpovědí
            if chosen_option == 1:
                correct_answers += 1

        # Zjištění, zda student odpověděl správně na alespoň polovinu otázek
        if correct_answers >= n / 2:
            successful_attempts += 1

    # Výpočet pravděpodobnosti
    probability = successful_attempts / count
    print(f"Experimental probability: {probability}")

# Příklad použití
simulate_test_probability(10, 10000)
