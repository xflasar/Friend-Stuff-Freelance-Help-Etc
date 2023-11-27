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

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(5, sorted_list)
print(result)  # Output: True
