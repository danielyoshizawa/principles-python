# Tuple

# Tuples are immutable sequences, meaning their contents cannot be changed after creation.
# They are defined using parentheses () or the tuple() constructor.

# Key characteristics of tuples:
# 1. Immutability: Once created, tuple elements cannot be modified, added, or removed.
# 2. Ordered: Elements in a tuple maintain their order and can be accessed by index.
# 3. Heterogeneous: Tuples can contain elements of different data types.
# 4. Duplicates: Tuples can contain duplicate elements.
# 5. Nestable: Tuples can contain other tuples or complex data structures.

# Example of creating a tuple:
my_tuple = (1, "hello", 3.14, True)

# Accessing tuple elements:
print(my_tuple[1])  # Output: "hello"

# Tuples are often used for:
# - Returning multiple values from functions
# - Creating immutable collections of related data
# - As dictionary keys (since they're immutable)
# - In sets (as they're hashable)

# While tuples are immutable, they can contain mutable objects:
nested_tuple = ([1, 2], {3, 4}, {"key": "value"})
# The tuple itself can't be changed, but its mutable elements can be modified.

# Tuple packing and unpacking:
a, b, c = (1, 2, 3)  # Unpacking
coordinates = 4, 5  # Packing (parentheses are optional)

print(coordinates)

# Tuples are memory-efficient and slightly faster than lists for read-only operations.

# Tuple indexing and slicing examples

# Create a sample tuple
sample_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Indexing examples
print("\nIndexing examples:")
print(f"First element: {sample_tuple[0]}")
print(f"Last element: {sample_tuple[-1]}")
print(f"Third element: {sample_tuple[2]}")

# Slicing examples
print("\nSlicing examples:")
print(f"First three elements: {sample_tuple[:3]}")
print(f"Last three elements: {sample_tuple[-3:]}")
print(f"Elements from index 2 to 5: {sample_tuple[2:6]}")
print(f"Every second element: {sample_tuple[::2]}")
print(f"Reversed tuple: {sample_tuple[::-1]}")

# Attempting to modify a tuple (will raise an error)
try:
    sample_tuple[0] = 10
except TypeError as e:
    print(f"\nAttempting to modify a tuple raises an error: {e}")

# Using tuple methods
print(f"\nCount of 3 in the tuple: {sample_tuple.count(3)}")
print(f"Index of 7 in the tuple: {sample_tuple.index(7)}")
