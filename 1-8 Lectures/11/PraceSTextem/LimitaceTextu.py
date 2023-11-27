import random

def get_next_word(text, current_word):
    next_words = []
    for i in range(len(text) - 1):
        if text[i] == current_word:
            next_words.append(text[i + 1])
    return next_words

def text_imitation(filename: str, length: int) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().lower().split()
        current_word = random.choice(words)

        for _ in range(length):
            print(current_word, end=' ')
            next_words = get_next_word(words, current_word)
            
            if not next_words:
                break  # Break if there are no more words following the current word
            current_word = random.choice(next_words)

# Test the function
text_imitation('devatero_pohadek.txt', 10)
