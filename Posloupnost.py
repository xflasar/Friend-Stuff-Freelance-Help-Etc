def sum_sequence(n):
  sequence = []

  for k in range(1, n + 1):
    sequence.append(sum(range(1, k + 1))) # append the sum of the range of 1 to k to the sequence

  print(" ".join(map(str, sequence))) # join the sequence elements with a space

# Test cases:
sum_sequence(6)