from random import randint
from typing import List

def dice() -> int:
    return randint(1, 6)

def dice_max(count: int) -> int:
    assert count >= 1, "The count parameter must be greater than or equal to 1."
    
    maximum = dice()
    for _ in range(count - 1):
        roll = dice()
        if roll > maximum:
            maximum = roll
    return maximum
