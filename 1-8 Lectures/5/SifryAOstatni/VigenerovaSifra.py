def vigenere_cipher(text, key):
    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            # Určení velikosti písmene
            is_upper = char.isupper()

            # Určení posunu na základě písmene z klíče
            shift = ord(key[key_index].upper()) - ord('A')

            # Posun v abecedě
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))

            result += shifted_char

            # Posun indexu klíče, pokud jsme na konci klíče
            key_index = (key_index + 1) % len(key)
        else:
            result += char

    return result

# Příklad použití
text_to_encrypt = "Hello, World!"
encryption_key = "KEY"

encrypted_text = vigenere_cipher(text_to_encrypt, encryption_key)

print(f"Text: {text_to_encrypt}")
print(f"Zašifrovaný text: {encrypted_text}")
