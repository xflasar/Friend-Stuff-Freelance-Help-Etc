import re

def is_integer(string: str) -> bool:
    pattern = re.compile(r'^[+-]?\d+$')

    match = pattern.match(string)

    return bool(match and match.group() == string)

# Test the function
def test_is_integer() -> None:
    assert is_integer("42") == True
    assert is_integer("-42") == True
    assert is_integer("4a2") == False

# Run the tests
test_is_integer()
