# Merge Sort

# Merge Sort is a divide-and-conquer algorithm that works as follows:
# 1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
# 2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # print(left, right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    # print(result)
    return result

# Example usage:
if __name__ == "__main__":
    example_array = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted array:", example_array)
    sorted_array = merge_sort(example_array)
    print("Sorted array:", sorted_array)

# Time Complexity: O(n log n) in all cases
# Space Complexity: O(n) due to the temporary arrays created during merging

# Merge Sort is stable, meaning that it preserves the relative order of equal elements.
# It's particularly useful for sorting linked lists and for external sorting (sorting data that doesn't fit into memory).
