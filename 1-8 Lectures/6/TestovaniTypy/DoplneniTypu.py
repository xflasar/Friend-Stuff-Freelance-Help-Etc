from random import randint
from typing import List

def dice() -> int:
    return randint(1, 6)

def dice_max(count: int) -> int:
    maximum = dice()
    for _ in range(count - 1):
        roll = dice()
        if roll > maximum:
            maximum = roll
    return maximum
