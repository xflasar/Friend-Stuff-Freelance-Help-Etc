MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", "0": "-----",
}

def encode(value: str) -> str:
    return ' '.join(MORSE_CODE[char] for char in value.upper() if char in MORSE_CODE)

def decode(value: str) -> str:
    morse_words = value.split(' ')
    reverse_morse_dict = {code: char for char, code in MORSE_CODE.items()}
    return ''.join(reverse_morse_dict[word] for word in morse_words if word in reverse_morse_dict)

def test_encode() -> None:
    assert encode('SOS') == "... --- ..."
    assert encode('HELLOWORLD') == ".... . .-.. .-.. --- .-- --- .-. .-.. -.."

def test_decode() -> None:
    assert decode('.... . .-.. .-.. --- .-- --- .-. .-.. -..') == "HELLOWORLD"
    assert decode(encode('IDENTITY')) == "IDENTITY"

# Run tests
test_encode()
test_decode()
