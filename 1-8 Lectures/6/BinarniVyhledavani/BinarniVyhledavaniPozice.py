def binary_search(needle, haystack):
    low, high = 0, len(haystack) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = haystack[mid]

        if guess == needle:
            return mid  # Found the element, return its index
        elif guess < needle:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

def test_binary_search_extended():
    # Test Case 1: Value is present in the middle of the list
    assert binary_search(3, [1, 2, 3, 4, 5]) == 2

    # Test Case 2: Value is present at the beginning of the list
    assert binary_search(1, [1, 2, 3, 4, 5]) == 0

    # Test Case 3: Value is present at the end of the list
    assert binary_search(5, [1, 2, 3, 4, 5]) == 4

    # Test Case 4: Value is not present in the list
    assert binary_search(6, [1, 2, 3, 4, 5]) == -1

    # Test Case 5: Empty list
    assert binary_search(1, []) == -1

    print("All tests passed successfully!")

# Run the test
test_binary_search_extended()
