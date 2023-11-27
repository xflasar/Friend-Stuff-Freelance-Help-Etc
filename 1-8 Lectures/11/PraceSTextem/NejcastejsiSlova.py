from collections import Counter
import re

def most_freq_words(filename: str) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w{3,}\b', text.lower())
        
        word_counts = Counter(words)
        most_common_words = word_counts.most_common(10)
        
        for word, count in most_common_words:
            print(f'{word}: {count}')

# Test the function
most_freq_words('sherlock-holmes.txt')
