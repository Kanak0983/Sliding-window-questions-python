def countDistinctElementsInWindow(arr, k):
    from collections import defaultdict
    
    # Hash map to store frequency of elements
    freq_map = defaultdict(int)
    distinct_count = 0
    result = []

    # Process the first window
    for i in range(k):
        if freq_map[arr[i]] == 0:
            distinct_count += 1
        freq_map[arr[i]] += 1
    
    result.append(distinct_count)

    # Slide the window
    for i in range(k, len(arr)):
        # Remove the element going out of the window
        if freq_map[arr[i - k]] == 1:
            distinct_count -= 1
        freq_map[arr[i - k]] -= 1

        # Add the new element entering the window
        if freq_map[arr[i]] == 0:
            distinct_count += 1
        freq_map[arr[i]] += 1

        result.append(distinct_count)

    return result

# Example usage:
arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
print(countDistinctElementsInWindow(arr, k))  # Output: [3, 4, 4, 3]
