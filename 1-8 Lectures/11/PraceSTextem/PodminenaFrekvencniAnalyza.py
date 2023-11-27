def cond_freq_analysis(filename: str) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert all characters to lowercase for case-insensitive analysis
        char_pairs = {}

        for i in range(len(text) - 1):
            char = text[i]
            next_char = text[i + 1]

            if char.isalpha() and next_char.isalpha():
                pair = (char, next_char)
                char_pairs[pair] = char_pairs.get(pair, 0) + 1

        # Print the conditional frequency analysis
        for char, next_char in sorted(char_pairs, key=lambda x: char_pairs[x], reverse=True):
            count = char_pairs[(char, next_char)]
            print(f'{char} -> {next_char}: {count}')

# Test the function
cond_freq_analysis('devatero_pohadek.txt')
