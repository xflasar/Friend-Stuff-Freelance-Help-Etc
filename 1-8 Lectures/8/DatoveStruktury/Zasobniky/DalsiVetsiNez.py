from typing import List, Tuple

def next_greater(lst: List[int]) -> List[Tuple[int, int]]:
    result = []
    stack = []

    for num in reversed(lst):
        while stack and stack[-1] <= num:
            stack.pop()

        ng = stack[-1] if stack else None
        result.append((num, ng))
        stack.append(num)

    return list(reversed(result))

# Příklad použití:
input_list = [4, 5, 2, 10, 8]
output = next_greater(input_list)
print(output)
