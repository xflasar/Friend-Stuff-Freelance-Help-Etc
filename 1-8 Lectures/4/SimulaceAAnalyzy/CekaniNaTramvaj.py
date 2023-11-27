import random

def wait_time_simulation(interval, count, w):
    wait_longer_count = 0

    for _ in range(count):
        # Simulace náhodného příchodu na zastávku
        arrival_time = random.uniform(0, interval)

        # Výpočet čekací doby
        wait_time = max(0, interval - arrival_time)

        # Kontrola, zda je čekací doba delší než w minut
        if wait_time > w:
            wait_longer_count += 1

    # Výpočet procentuálního podílu případů, kdy čekáte déle než w minut
    percentage_waiting_longer = (wait_longer_count / count) * 100
    print(f"Percentage of cases waiting longer than {w} minutes: {percentage_waiting_longer}%")

# Příklad použití
wait_time_simulation(10, 1000, 5)
