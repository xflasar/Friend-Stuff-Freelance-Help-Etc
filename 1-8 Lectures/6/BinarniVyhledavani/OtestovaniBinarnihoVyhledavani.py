def binary_search(needle, haystack):
    low, high = 0, len(haystack) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = haystack[mid]

        if guess == needle:
            return True
        elif guess < needle:
            low = mid + 1
        else:
            high = mid - 1

    return False

def test_binary_search_extended():
    # Test Case 1: Value is present in the middle of the list
    assert binary_search(3, [1, 2, 3, 4, 5]) == True

    # Test Case 2: Value is present at the beginning of the list
    assert binary_search(1, [1, 2, 3, 4, 5]) == True

    # Test Case 3: Value is present at the end of the list
    assert binary_search(5, [1, 2, 3, 4, 5]) == True

    # Test Case 4: Value is not present in the list
    assert binary_search(6, [1, 2, 3, 4, 5]) == False

    # Test Case 5: Empty list
    assert binary_search(1, []) == False

    print("All tests passed successfully!")

# Run the test
test_binary_search_extended()
