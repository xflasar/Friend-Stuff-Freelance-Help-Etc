import random

def roll_and_count_dice_pairs(count):
    frequency_counter = {i: 0 for i in range(2, 13)}

    for _ in range(count):
        roll_result_1 = random.randint(1, 6)
        roll_result_2 = random.randint(1, 6)
        total_sum = roll_result_1 + roll_result_2
        frequency_counter[total_sum] += 1

    # Vypisujeme frekvence jednotlivých součtů
    for total_sum, frequency in frequency_counter.items():
        print(f"Součet {total_sum}: {frequency}x")

# Příklad použití
roll_and_count_dice_pairs(100)
