def series_sum(n: int) -> int:
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return n + series_sum(n - 1)

def test_series_sum() -> None:
    assert series_sum(1) == 1
    assert series_sum(5) == 15
    assert series_sum(10) == 55
    assert series_sum(100) == 5050

# Run the test
test_series_sum()
