def capitalize_words(input_string):
    # Rozdělíme vstupní řetězec na slova
    words = input_string.split()

    # Kapitalizujeme každé slovo
    capitalized_words = [word.capitalize() for word in words]

    # Sestavíme nový řetězec spojením kapitalizovaných slov mezerou
    result_string = ' '.join(capitalized_words)

    return result_string

# Příklad použití
input_text = "hello world"
capitalized_text = capitalize_words(input_text)

print(f"Vstupní text: {input_text}")
print(f"Kapitalizovaný text: {capitalized_text}")
