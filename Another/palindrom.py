def palindrom(text):
  text = text.lower()
  for i in range(len(text)//2):
    if text[i] != text[len(text)-i-1]:
      return False
  return True

# Test Cases:
print(palindrom("jelenovipivonelej"))
print(palindrom("prase"))
print(palindrom("anna"))
print(palindrom("franta"))