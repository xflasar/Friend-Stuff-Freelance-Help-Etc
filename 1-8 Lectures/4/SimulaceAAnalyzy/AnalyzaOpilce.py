import random

def drunkman_simulator(distance, max_steps, output=True):
    home = "home"
    pub = "pub"
    current_position = distance // 2  # Opilec začíná na půli cesty

    for step in range(max_steps):
        # Náhodně určujeme směr kroku
        direction = random.choice([-1, 1])
        current_position += direction

        # Kontrola, zda opilec došel domů nebo do hospody
        if current_position == 0:
            if output:
                print("Ended at home!")
            return True
        elif current_position == distance - 1:
            if output:
                print("Ended in the pub again!")
            return False

    # Opilec nedošel ani domů, ani do hospody
    if output:
        print("Simulation ended without reaching home or pub.")
    return False

def simulate_multiple_times(distance, max_steps, count):
    successes = 0

    for _ in range(count):
        if drunkman_simulator(distance, max_steps, output=False):
            successes += 1

    success_percentage = (successes / count) * 100
    print(f"Success rate: {success_percentage}%")

# Příklad použití
simulate_multiple_times(10, 100, 1000)
