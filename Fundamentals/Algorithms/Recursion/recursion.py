# Recursion

# Recursion is a programming concept where a function calls itself to solve a problem.
# It's particularly useful for tasks that can be broken down into smaller, similar sub-problems.

# Key components of a recursive function:
# 1. Base case: A condition that stops the recursion
# 2. Recursive case: Where the function calls itself with a modified input

# Example 1: Factorial calculation

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Example usage:
print("Factorial Example:")
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")

# Example 2: Fibonacci sequence

def fibonacci(n):
    # Base cases
    if n <= 1:
        return n
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
print("\nFibonacci Example:")
print(f"5th Fibonacci number: {fibonacci(5)}")
print(f"8th Fibonacci number: {fibonacci(8)}")

# Example 3: Recursive sum of a list

def list_sum(lst):
    # Base case
    if not lst:
        return 0
    # Recursive case
    else:
        return lst[0] + list_sum(lst[1:])

# Example usage:
print("\nList Sum Example:")
print(f"Sum of [1, 2, 3, 4, 5]: {list_sum([1, 2, 3, 4, 5])}")
print(f"Sum of []: {list_sum([])}")

# Example 4: Recursive binary search

def binary_search(arr, target, low, high):
    # Base case: target not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # Base case: target found
    if arr[mid] == target:
        return mid
    # Recursive cases
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

# Example usage:
print("\nBinary Search Example:")
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(sorted_list, target, 0, len(sorted_list) - 1)
print(f"Index of {target} in {sorted_list}: {result}")

# Note: While recursion can lead to elegant solutions, it can also be memory-intensive
# for deep recursions due to the call stack. In such cases, an iterative approach
# or tail-recursion optimization might be preferred.

# Exercise for the reader:
# 1. Implement a recursive function to calculate the power of a number (x^n)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print("Power of 2^3: {}".format(power(2, 3)))

# 2. Write a recursive function to reverse a string

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print("Reverse of 'hello': {}".format(reverse_string("hello")))

# 3. Create a recursive solution for the Tower of Hanoi problem

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        tower_of_hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')
