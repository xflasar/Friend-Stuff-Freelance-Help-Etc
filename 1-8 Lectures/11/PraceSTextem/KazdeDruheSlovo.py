import re

def every_second(filename: str) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        
        for i in range(1, len(words), 2):
            print(words[i], end=' ')

# Test the function
every_second("lorem-ipsum.txt")
