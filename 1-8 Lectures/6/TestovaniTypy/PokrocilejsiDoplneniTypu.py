from random import randint
from typing import Optional

def dice() -> int:
    return randint(1, 6)

def dice_max(count: int) -> Optional[int]:
    assert count >= 0, "The count parameter must be greater than or equal to 0."

    if count == 0:
        return None

    maximum = dice()
    for _ in range(count - 1):
        roll = dice()
        if roll > maximum:
            maximum = roll
    return maximum
