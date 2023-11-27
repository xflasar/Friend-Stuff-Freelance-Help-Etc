def freq_analysis(text: str) -> None:
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = ' '.join(word.lower() for word in text.split() if word.isalpha())

    # Count the frequency of each word
    word_freq = {}
    for word in cleaned_text.split():
        word_freq[word] = word_freq.get(word, 0) + 1

    # Sort the words alphabetically
    sorted_words = sorted(word_freq.items(), key=lambda x: x[0])

    # Print the sorted frequencies
    for word, freq in sorted_words:
        print(f"{word}: {freq}")

# Example usage
dummy = """Monty Python and Monty Python all over here."""
freq_analysis(dummy)
