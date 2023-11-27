from typing import List

def quick_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Test the function
def test_quick_sort() -> None:
    assert quick_sort([2, 7, 8, 1, 4, 5, 9, 3, 6]) == list(range(1, 10))

test_quick_sort()
