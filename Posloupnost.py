def sum_sequence(n):
  sequence = []

  for k in range(1, n + 1):
    sequence.append(sum(range(1, k + 1)))

  print(" ".join(map(str, sequence)))

# Test cases:
sum_sequence(6)