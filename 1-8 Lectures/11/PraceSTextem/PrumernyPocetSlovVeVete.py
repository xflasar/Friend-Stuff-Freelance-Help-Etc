import re

def average_sentence_len(filename: str) -> float:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        sentences = re.split(r'[.!?]', text)
        
        # Remove empty strings from the list
        sentences = list(filter(None, sentences))
        
        # Calculate the average number of words per sentence
        total_words = sum(len(re.findall(r'\b\w+\b', sentence)) for sentence in sentences)
        total_sentences = len(sentences)
        
        if total_sentences == 0:
            return 0.0
        
        return total_words / total_sentences

# Test the function
print(average_sentence_len('alice-in-wonderland.txt'))
