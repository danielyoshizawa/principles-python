# Quick Sort

# Quick Sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element
# from the array and partitioning the other elements into two sub-arrays, according to
# whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

# Here's how it works:
# 1. Choose a pivot element from the array.
# 2. Partition the array around the pivot, moving smaller elements to the left and larger to the right.
# 3. Recursively apply the above steps to the sub-arrays on the left and right of the pivot.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage:
example_array = [3, 6, 8, 10, 1, 2, 1]
# pivot = 8
# left = [3, 6, 1, 2, 1]
# middle = [8]
# right = [10]
# [3, 6, 1, 2, 1] + [8] + [10]
# pivot = 1
# left = []
# middle = [1, 1]
# right = [3, 6]
# [] + [1, 1] + [2] + [3, 6] + [8] + [10]
# pivot = 3
# left = []
# middle = [3]
# right = [6]
# [] + [1, 1] + [2] + [3] + [6] + [8] + [10]
# pivot = 1
# left = []
# middle = [1]
# right = []
# [] + [1] + [1] + [2] + [3] + [6] + [8] + [10]

print("Unsorted array:", example_array)
sorted_array = quicksort(example_array)
print("Sorted array:", sorted_array)

# Let's implement an in-place version of quicksort for better space efficiency:

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)

# Example usage of in-place quicksort:
example_array_2 = [64, 34, 25, 12, 22, 11, 90]
print("\nUnsorted array for in-place sort:", example_array_2)
quicksort_inplace(example_array_2, 0, len(example_array_2) - 1)
print("Sorted array after in-place sort:", example_array_2)

# Time Complexity: 
# - Average and Best Case: O(n log n)
# - Worst Case: O(n^2) (when the pivot is always the smallest or largest element)

# Space Complexity:
# - O(log n) for the recursive call stack in the average case
# - O(n) in the worst case for the recursive call stack

# Quick Sort is often faster in practice compared to other O(n log n) algorithms
# like Merge Sort, especially for smaller datasets, due to its in-place nature
# and good cache performance.
