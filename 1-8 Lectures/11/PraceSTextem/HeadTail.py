def head(filename: str, n: int) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        for _ in range(n):
            line = file.readline().rstrip()
            if not line:
                break
            print(line)

def tail(filename: str, n: int) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        total_lines = len(lines)
        start_index = max(0, total_lines - n)

        for i in range(start_index, total_lines):
            print(lines[i].rstrip())

# Test the functions
head("alice-in-wonderland.txt", 3)
print()
tail("alice-in-wonderland.txt", 3)
