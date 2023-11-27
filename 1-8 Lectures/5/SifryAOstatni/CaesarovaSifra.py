def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Určení velikosti písmene
            is_upper = char.isupper()

            # Posun v abecedě
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))

            result += shifted_char
        else:
            result += char

    return result

# Příklad použití
text_to_encrypt = "Hello, World!"
shift_amount = 3

encrypted_text = caesar_cipher(text_to_encrypt, shift_amount)

print(f"Text: {text_to_encrypt}")
print(f"Zašifrovaný text: {encrypted_text}")
