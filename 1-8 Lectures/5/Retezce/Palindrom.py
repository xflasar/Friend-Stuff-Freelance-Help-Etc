def is_palindrome(s):
    # Odstraníme mezery ze vstupního řetězce a převedeme na malá písmena
    s = s.replace(" ", "").lower()

    # Porovnáme řetězec s jeho obrácením
    return s == s[::-1]

# Příklad použití
word = "nepotopen"
result = is_palindrome(word)

if result:
    print(f"{word} je palindrom.")
else:
    print(f"{word} není palindrom.")
