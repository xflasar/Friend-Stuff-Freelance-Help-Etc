def frame(text, symbol):
  part1 = symbol * (len(text) + 2)
  part2 = symbol + text + symbol
  part3 = symbol * (len(text) + 2)
  print(part1+ "\n" + part2 + "\n" + part3)

  for row in range(3):
    if row == 0 or row == 2:
      print(symbol * (len(text) + 2))
    else:
      print(symbol + text + symbol)
    

frame("R2D2", "*")
print()
frame("Millennium Falcon", "=")