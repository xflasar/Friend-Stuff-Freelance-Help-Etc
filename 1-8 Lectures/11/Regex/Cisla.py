import re

def is_number(string: str) -> bool:
    pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)$')

    return bool(pattern.fullmatch(string))

# Get user input
user_input = input("Enter a string to check if it is a number: ")

# Check if the input is a number
if is_number(user_input):
    print(f"{user_input} is a number.")
else:
    print(f"{user_input} is not a number.")
