from typing import List

def sudoku_line_check(line: List[int]) -> bool:
    # Check if the line has exactly 9 elements
    if len(line) != 9:
        return False

    # Check if all elements are between 1 and 9 (inclusive) and unique
    return all(1 <= num <= 9 for num in line) and len(set(line)) == 9

def test_sudoku_line_check() -> None:
    assert sudoku_line_check([1, 2, 8, 9, 3, 5, 6, 7, 4]) == True
    assert sudoku_line_check([1, 2, 8, 9, 3, 5, 7, 4]) == False
    assert sudoku_line_check([1, 1, 2, 8, 9, 3, 5, 7, 4]) == False
    assert sudoku_line_check([0, 1, 2, 3, 4, 5, 6, 7, 8]) == False

# Run the test
test_sudoku_line_check()
