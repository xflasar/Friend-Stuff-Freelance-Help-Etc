def freq_analysis(text: str) -> None:
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())

    # Count the frequency of each character
    char_freq = {}
    for char in cleaned_text:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Sort the characters by frequency in descending order
    sorted_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted frequencies
    for char, freq in sorted_freq:
        print(f"{char}: {freq}")

# Example usage
dummy = """Monty Python and Monty Python all over here."""
freq_analysis(dummy)
