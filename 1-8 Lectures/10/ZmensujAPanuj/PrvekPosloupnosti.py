def sequence(n: int) -> int:
    # Base case
    if n == 0:
        return 5
    # Recursive case
    return 2 * sequence(n - 1) - 1

# Test the function
assert sequence(0) == 5
assert sequence(1) == 9
assert sequence(2) == 17
assert sequence(3) == 33
