import re

def is_integer(string: str) -> bool:
    # Regular expression pattern for matching integers
    pattern = re.compile(r'^[+-]?\d+$')

    # Use the match function to check if the entire string matches the pattern
    match = pattern.match(string)

    # If there is a match and the match covers the entire string, return True
    return bool(match and match.group() == string)

# Test the function
def test_is_integer() -> None:
    assert is_integer("42") == True
    assert is_integer("-42") == True
    assert is_integer("4a2") == False

# Run the tests
test_is_integer()
