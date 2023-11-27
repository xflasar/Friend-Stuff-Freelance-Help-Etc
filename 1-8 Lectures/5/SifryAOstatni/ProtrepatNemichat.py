def reverse_tuples(text, n):
    result = ""

    for i in range(0, len(text), n):
        # Otočení n-tice pozpátku
        reversed_tuple = text[i:i + n][::-1]

        result += reversed_tuple

    return result

# Příklad použití
original_text = "abcdefghij"
n_value = 3

result_text = reverse_tuples(original_text, n_value)

print(f"Text: {original_text}")
print(f"Výsledek: {result_text}")
