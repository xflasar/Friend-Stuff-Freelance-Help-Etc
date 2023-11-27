def hanoi(n: int, source: str, target: str, auxiliary: str) -> None:
    if n == 1:
        print(f"{source} -> {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"{source} -> {target}")
        hanoi(n - 1, auxiliary, target, source)

# Test the function
hanoi(3, 'A', 'C', 'B')
