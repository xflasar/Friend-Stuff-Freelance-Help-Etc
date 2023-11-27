from typing import List

def unique_check(temp: List[int]) -> bool:
    # Use a set to keep track of unique elements
    unique_elements = set()

    # Iterate through the list
    for element in temp:
        # If the element is already in the set, it's not unique
        if element in unique_elements:
            return False
        # Otherwise, add it to the set
        else:
            unique_elements.add(element)

    # If the loop completes, all elements are unique
    return True

def test_unique_check():
    assert unique_check([1, 5, 6, 5, 4, 9]) == False
    assert unique_check([1, 5, 6, 3, 9]) == True

# Run the test
test_unique_check()
