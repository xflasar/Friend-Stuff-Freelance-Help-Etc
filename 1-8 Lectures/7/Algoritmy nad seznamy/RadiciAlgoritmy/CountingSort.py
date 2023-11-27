def counting_sort(arr):
    if not arr:
        return arr

    # Find the maximum value in the array
    max_value = max(arr)

    # Initialize a count array with zeros
    count = [0] * (max_value + 1)

    # Count occurrences of each element in the array
    for num in arr:
        count[num] += 1

    # Generate the sorted array using the count array
    sorted_array = []
    for i in range(len(count)):
        sorted_array.extend([i] * count[i])

    return sorted_array

# Example usage:
unsorted_array = [3, 6, 2, 8, 3, 1, 2]
sorted_array = counting_sort(unsorted_array)
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
