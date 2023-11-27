# BROKEN!!!

def hanoi(n: int, source: str, target: str, auxiliary: str) -> None:
    def print_state(towers):
        for level in zip(*towers):
            print(" ".join(level))

    towers = {
        source: [f"{'#' * (2 * i + 1):^6}" for i in range(n, 0, -1)] + ["-" * 6] * (n - 1),
        auxiliary: [" " * 6] * n + ["-" * 6] * (n - 1),
        target: [" " * 6] * n + ["-" * 6] * (n - 1),
    }

    print_state(towers)

    def move_disc(src, tgt):
        disc = towers[src].pop()
        towers[tgt].append(disc)
        print_state(towers)

    def hanoi_recursive(k, source, target, auxiliary):
        if k == 1:
            move_disc(source, target)
        else:
            hanoi_recursive(k - 1, source, auxiliary, target)
            move_disc(source, target)
            hanoi_recursive(k - 1, auxiliary, target, source)

    hanoi_recursive(n, source, target, auxiliary)

# Test the function
hanoi(3, 'A', 'C', 'B')

## BROKEN BUt yeaheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee