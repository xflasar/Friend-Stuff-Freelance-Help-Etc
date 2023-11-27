import random
import math

def random_point_in_square(size):
    x = random.uniform(0, size)
    y = random.uniform(0, size)
    return x, y

def distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def average_distance_simulation(size, count):
    total_distance = 0

    for _ in range(count):
        # Náhodný výběr dvou bodů
        point1 = random_point_in_square(size)
        point2 = random_point_in_square(size)

        # Výpočet vzdálenosti mezi body
        distance = distance_between_points(point1, point2)

        # Přičtení vzdálenosti k celkové vzdálenosti
        total_distance += distance

    # Výpočet průměrné vzdálenosti
    average_distance = total_distance / count
    print(f"Average distance over {count} simulations: {average_distance}")

# Příklad použití
average_distance_simulation(10, 1000)
