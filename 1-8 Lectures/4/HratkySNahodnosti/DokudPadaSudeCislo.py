import random

def roll_until_odd():
    total_sum = 0

    while True:
        roll_result = random.randint(1, 6)
        total_sum += roll_result

        if roll_result % 2 == 1:
            break  # Pokud padne liché číslo, ukončí smyčku

    return total_sum

# Příklad použití
result_sum = roll_until_odd()
print(f"Celkový součet hodů do prvního lichého čísla: {result_sum}")
