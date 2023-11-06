def duplication(text):
    textResult = ''
    for char in text:
      textResult += char * 2

    return textResult

# Test Cases:
print(duplication("PYTHON"))