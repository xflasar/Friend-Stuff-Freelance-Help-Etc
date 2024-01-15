# Otevřeme soubor, odstraníme non-alphabetic znaky a vrátíme seznam slov. 
# Načteme seznam slov a vytvoříme seznam n-gramů poté použijeme Counter z collection library kde vytvoříme slovník s n-gramy a jejich četností.

import re
from collections import Counter

def load_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
    return words

def analyze_n_gram(n: int, k: int, filename: str) -> None:
    words = load_file(filename)

    ngrams = [word[i:i+n] for word in words for i in range(len(word)-n+1)]

    ngram_counts = Counter(ngrams)

    print(f"The {k} most frequent {n}-grams are:")
    for ngram, count in ngram_counts.most_common(k):
        print(f"{ngram}: {count} occurrences")

analyze_n_gram(5, 8, 'alice-in-wonderland.txt')
