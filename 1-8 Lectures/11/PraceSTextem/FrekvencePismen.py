def freq_analysis(filename: str) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        letter_count = {}

        for char in text:
            if char.isalpha():
                letter_count[char] = letter_count.get(char, 0) + 1

        for letter, count in sorted(letter_count.items()):
            print(f'{letter}: {count}')

# Test the function
freq_analysis('alice-in-wonderland.txt')
