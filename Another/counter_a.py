def count_a(text):
  a_count = 0
  text = text.lower()

  for letter in text:
    if letter == 'a':
      a_count += 1
  
  return a_count

# Test Cases:
print(count_a("Abeceda")) # should print 2
print(count_a("slon")) # should print 0
print(count_a("prase")) # should print 1