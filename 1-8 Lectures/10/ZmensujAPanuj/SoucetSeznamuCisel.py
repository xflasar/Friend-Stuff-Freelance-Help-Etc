from typing import List

def list_sum(numbers: List[int]) -> int:
    # Base case: if the list is empty, the sum is 0
    if not numbers:
        return 0
    # Recursive case: sum the first element and the sum of the rest of the list
    return numbers[0] + list_sum(numbers[1:])

# Test the function
def test_list_sum() -> None:
    assert list_sum([1, 8, 2, 0, 4, 2]) == 17

test_list_sum()
