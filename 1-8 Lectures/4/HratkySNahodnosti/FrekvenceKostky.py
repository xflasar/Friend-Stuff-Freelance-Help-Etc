import random

def roll_and_count_dice(count):
    frequency_counter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(count):
        roll_result = random.randint(1, 6)
        frequency_counter[roll_result] += 1

    # Vypisujeme frekvence jednotlivých čísel
    for number, frequency in frequency_counter.items():
        print(f"Číslo {number}: {frequency}x")

# Příklad použití
roll_and_count_dice(100)
