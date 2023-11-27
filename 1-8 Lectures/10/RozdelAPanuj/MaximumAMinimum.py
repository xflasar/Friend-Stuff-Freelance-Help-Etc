from typing import List, Tuple

def min_max(numbers: List[int]) -> Tuple[int, int]:
    def find_min_max(start, end):
        if start == end:
            return numbers[start], numbers[start]

        mid = (start + end) // 2
        left_min, left_max = find_min_max(start, mid)
        right_min, right_max = find_min_max(mid + 1, end)

        return min(left_min, right_min), max(left_max, right_max)

    if not numbers:
        return None, None

    return find_min_max(0, len(numbers) - 1)

# Test the function
def test_min_max() -> None:
    assert min_max([8, 4, 3, 5, 9, 2, 1, 7, 6]) == (1, 9)

test_min_max()
