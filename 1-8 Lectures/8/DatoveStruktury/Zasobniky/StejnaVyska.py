from typing import List, Tuple

def equal_height(t1: List[int], t2: List[int], t3: List[int]) -> List[List[int]]:
    towers = [t1, t2, t3]

    # Function to check if all towers have the same height
    def is_equal_height():
        return all(len(set(tower)) == 1 for tower in towers)

    while not is_equal_height():
        for src, dest in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]:
            if towers[src] and (not towers[dest] or towers[src][-1] < towers[dest][-1]):
                towers[dest].append(towers[src].pop())

    return towers

# Example usage:
t1 = [3, 2, 1]
t2 = []
t3 = []

result = equal_height(t1, t2, t3)
print(result)
