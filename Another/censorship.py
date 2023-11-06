def censorship(text):
  text = list(text)
  for index in range(len(text)):
      if index % 2:
          text[index] = 'X'
          
  return ''.join(text)

# Test Cases:
print(censorship("Tajna zprava"))