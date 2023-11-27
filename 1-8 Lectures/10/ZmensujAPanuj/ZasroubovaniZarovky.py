def screwing(n: int) -> None:
    # Base case
    if n == 0:
        return
    # Recursive case
    print("twist")
    screwing(n - 1)

# Test the function
screwing(3)
