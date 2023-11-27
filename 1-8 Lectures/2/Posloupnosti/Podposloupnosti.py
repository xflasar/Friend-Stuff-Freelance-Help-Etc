def special_sequence(n):
    sequence = []
    i = 1
    while len(sequence) < n:
        for j in range(1, i + 1):
            sequence.append(j)
        i += 1
    return sequence[:n]

# Example usage to print the first 10 elements of the sequence
n = 10
result_sequence = special_sequence(n)
print(result_sequence)
