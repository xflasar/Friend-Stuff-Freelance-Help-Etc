import random

def drunkman_simulator(distance, max_steps):
    home = "home"
    pub = "pub"
    current_position = distance // 2  # Opilec začíná na půli cesty
    path = [home]  # Začínáme doma

    for step in range(max_steps):
        # Náhodně určujeme směr kroku
        direction = random.choice([-1, 1])
        current_position += direction

        # Zaznamenáváme aktuální pozici
        if current_position < 0:
            current_position = 0
        elif current_position >= distance:
            current_position = distance - 1

        # Přidáváme aktuální pozici do trasy
        path.append("home" + "." * current_position + "*" + "." * (distance - current_position - 1) + "pub")

        # Kontrola, zda opilec došel domů nebo do hospody
        if current_position == 0:
            path.append(home)
            path.append("Ended at home!")
            break
        elif current_position == distance - 1:
            path.append(pub)
            path.append("Ended in the pub again!")
            break

    return path

# Příklad použití
result = drunkman_simulator(10, 100)
for step in result:
    print(step)
