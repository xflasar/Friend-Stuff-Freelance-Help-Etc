import random

def find_treasure(width, steps):
    # Náhodně umístíme poklad na pozici [treasure_x, treasure_y]
    treasure_x = random.randint(0, width - 1)
    treasure_y = random.randint(0, width - 1)

    # Hledač začíná na pozici [0, 0]
    hunter_x, hunter_y = 0, 0

    for step in range(steps):
        # Náhodně zvolíme směr pohybu
        direction = random.choice(["up", "down", "left", "right"])

        # Aktualizujeme pozici hledače podle směru
        if direction == "up" and hunter_y > 0:
            hunter_y -= 1
        elif direction == "down" and hunter_y < width - 1:
            hunter_y += 1
        elif direction == "left" and hunter_x > 0:
            hunter_x -= 1
        elif direction == "right" and hunter_x < width - 1:
            hunter_x += 1

        # Zkontrolujeme, zda hledač nalezl poklad
        if hunter_x == treasure_x and hunter_y == treasure_y:
            return True

    # Hledač nepřišel na poklad
    return False

def simulate_treasure_hunt(width, steps, count):
    successes = 0

    for _ in range(count):
        if find_treasure(width, steps):
            successes += 1

    success_percentage = (successes / count) * 100
    print(f"Success rate: {success_percentage}%")

# Příklad použití
simulate_treasure_hunt(5, 20, 1000)
