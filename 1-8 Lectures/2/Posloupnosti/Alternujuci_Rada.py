def special_sequence(n):
    sequence = []
    i = 1
    while len(sequence) < 2 * n:
        sequence.append(i)
        sequence.append(-i)
        i += 1
    return sequence[:n]

# Example usage to print the first 10 elements of the sequence
n = 10
result_sequence = special_sequence(n)
print(result_sequence)
