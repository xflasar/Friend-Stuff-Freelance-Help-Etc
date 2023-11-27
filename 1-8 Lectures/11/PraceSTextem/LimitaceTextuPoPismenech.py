import random

def get_next_char(text, current_char):
    next_chars = []
    for i in range(len(text) - 1):
        word = text[i]
        if current_char in word and len(word) > len(current_char):
            next_chars.append(word[len(current_char)])
    return next_chars

def text_imitation(filename: str, length: int) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        words = [word.lower() for word in file.read().split()]
        current_char = random.choice('abcdefghijklmnopqrstuvwxyz')

        for _ in range(length):
            print(current_char, end='')
            next_chars = get_next_char(words, current_char)
            
            if not next_chars:
                break  # Break if there are no more characters following the current character
            current_char = random.choice(next_chars)

# Test the function
text_imitation('devatero_pohadek.txt', 50)
