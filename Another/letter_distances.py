def letter_distances(text):
  distances = []
  for i in range(len(text) - 1):
    distances.append(abs(ord(text[i]) - ord(text[i+1])))
  print(distances)

# Test Cases: 
letter_distances("KRABICE")