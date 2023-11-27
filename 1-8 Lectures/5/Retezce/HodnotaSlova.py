def calculate_string_value(s):
    # Ignorujeme diakritiku a převedeme na velká písmena
    s = s.upper()

    # Inicializujeme hodnotu na 0
    value = 0

    # Pro každý znak v řetězci
    for char in s:
        # Pokud je znak písmeno A-Z
        if 'A' <= char <= 'Z':
            # Přičteme hodnotu písmena (kde A=1, B=2, atd.)
            value += ord(char) - ord('A') + 1

    return value

# Příklad použití
word = "HELLO"
result = calculate_string_value(word)

print(f"Hodnota řetězce '{word}' je: {result}")
