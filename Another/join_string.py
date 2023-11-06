def join(text1, text2):
  if len(text1) < len(text2):
    return text1 + text2
  elif len(text1) > len(text2):
    return text2 + text1
  else:
    return text1 + text2

# Test
print(join("abcd", "efg"))
print(join("pes", "sova"))