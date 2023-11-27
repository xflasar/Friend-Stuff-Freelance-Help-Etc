def insert_text_between_letters(original_text, inserted_text):
    # Vytvoříme nový řetězec a vložíme dodaný text mezi každá dvě písmena
    result_text = inserted_text.join(original_text[i:i+2] for i in range(0, len(original_text), 2))
    return result_text

# Příklad použití
original_text = "abcdefgh"
inserted_text = "X"
result = insert_text_between_letters(original_text, inserted_text)

print("Původní text:", original_text)
print("Text po vložení:", result)
