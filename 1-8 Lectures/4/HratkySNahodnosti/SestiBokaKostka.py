import random

def roll_dice():
    return random.randint(1, 6)

# Příklad použití
result = roll_dice()
print(f"Hod kostkou: {result}")
