import random
import string

def generate_random_string(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

# Příklad použití
allowed_chars = string.ascii_letters + string.digits  # Používáme písmena a číslice
random_string = generate_random_string(10, allowed_chars)

print(f"Náhodný řetězec: {random_string}")
