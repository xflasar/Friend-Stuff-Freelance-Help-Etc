from typing import List

def binary_search(value: int, numbers: List[int]) -> bool:
    def binary_search_helper(left: int, right: int) -> bool:
        if left > right:
            return False

        mid = (left + right) // 2
        if numbers[mid] == value:
            return True
        elif numbers[mid] < value:
            return binary_search_helper(mid + 1, right)
        else:
            return binary_search_helper(left, mid - 1)

    return binary_search_helper(0, len(numbers) - 1)

# Test the function
def test_binary_search() -> None:
    assert binary_search(5, [1, 2, 5, 8]) == True
    assert binary_search(4, [1, 2, 5, 8]) == False

test_binary_search()
