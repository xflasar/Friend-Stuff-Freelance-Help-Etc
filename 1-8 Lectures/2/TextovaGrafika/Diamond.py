def diamond(n):
    for i in range(n):
        row = " " * (n - i - 1) + "#" * (2 * i + 1)
        print(row)

    for i in range(n - 2, -1, -1):
        row = " " * (n - i - 1) + "#" * (2 * i + 1)
        print(row)

# Example usage to draw a diamond pattern with side length 5
diamond(5)