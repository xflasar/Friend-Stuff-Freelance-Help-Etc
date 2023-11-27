def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage:
unsorted_array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = merge_sort(unsorted_array)
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
