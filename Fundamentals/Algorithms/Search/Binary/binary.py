# Binary Search

# Binary Search is an efficient algorithm for searching a sorted array by repeatedly
# dividing the search interval in half. It works as follows:
# 1. Begin with the mid element of the whole array as a search key.
# 2. If the value of the search key is equal to the item then return an index of the search key.
# 3. Or if the value of the search key is less than the item in the middle of the interval,
#    narrow the interval to the lower half.
# 4. Otherwise, narrow it to the upper half.
# 5. Repeatedly check from step 2 until the value is found or the interval is empty.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Example usage:
if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    target = 7
    result = binary_search(sorted_array, target)
    
    if result != -1:
        print(f"Element {target} is present at index {result}")
    else:
        print(f"Element {target} is not present in array")

    # More examples
    print(binary_search(sorted_array, 1))  # Should return 0
    print(binary_search(sorted_array, 15))  # Should return 7
    print(binary_search(sorted_array, 10))  # Should return -1

# Time Complexity: O(log n) - where n is the number of elements in the array
# Space Complexity: O(1) - as it uses only a constant amount of additional space

# Note: Binary search requires the array to be sorted beforehand.
# It's much faster than linear search for large datasets, but for very small arrays,
# linear search might be faster due to less overhead.
