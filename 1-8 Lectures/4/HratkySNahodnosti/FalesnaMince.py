import random

def simulate_fake_coin_toss():
    # Generujeme náhodné číslo mezi 0 a 1
    toss_result = random.random()

    # Definujeme pravděpodobnosti pro hlavu a orel
    probability_heads = 0.85

    # Rozhodujeme, jestli padla hlava nebo orel
    result = toss_result < probability_heads

    return result

# Příklad použití
for _ in range(10):
    outcome = simulate_fake_coin_toss()
    print("Hlava" if outcome else "Orel")
