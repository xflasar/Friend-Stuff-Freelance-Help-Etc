def first_letters(text):

  textArr = text.split()
  for i in range(len(textArr)):
    print(textArr[i][0] + " ", end="")
  print()

  # textArr = text.split()
  #   first_letters = [word[0] for word in textArr]
  #   return ''.join(first_letters)



# Test Cases:
first_letters("jedna dva tri ctyri pet")
first_letters("pozor na  vice mezer")