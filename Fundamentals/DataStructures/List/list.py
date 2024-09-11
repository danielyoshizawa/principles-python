# List

# List is a collection which is ordered and changeable (mutable). Allows duplicate members.
# List is created using square brackets []

# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Key Features:
# - Allows duplicate members
# - Ordered
# - Supports indexing and slicing
# - Mutable
# - Dynamic size
# - Heterogeneous (can contain elements of different types)
# - Can be nested
# - Can be heterogeneous

# Accessing elements

print(my_list[0])

# Slicing
# Slicing is a way to access a range of elements from a list.
# It is done using the colon operator :
# The syntax is list[start:end]
# The start is inclusive and the end is exclusive

print(my_list[1:3])

# Negative indexing
# Negative indexing is a way to access elements from the end of the list.
# It is done using negative indices.
# The last element is at index -1, the second last element is at index -2, and so on.

print(my_list[-1])


# Modifying elements
# We can modify elements in a list by assigning a new value to a specific index.

my_list[0] = 10
print(my_list)

# Adding elements
# We can add elements to a list by using the append method.

my_list.append(6)
print(my_list)

# We can also add elements to a list by using the extend method.
# The extend method takes a list as an argument and adds its elements to the end of the list.
# The elements are added in the order they appear in the argument list.

my_list.extend([7, 8, 9])
print(my_list)

# Removing elements
# We can remove elements from a list by using the remove method.
# The remove method takes an element as an argument and removes the first occurrence of that element from the list.

my_list.remove(3)
print(my_list)

# We can also remove elements from a list by using the pop method.
# The pop method takes an index as an argument and removes the element at that index from the list.
# The index is optional and if not provided, the last element is removed.

my_list.pop(0)
print(my_list)

# We can also remove elements from a list by using the del statement.
# The del statement takes an index as an argument and removes the element at that index from the list.
# The index is optional and if not provided, all elements are removed from the list.

del my_list[0]
print(my_list)

# We can also remove elements from a list by using the clear method.
# The clear method removes all elements from the list.

my_list.clear()
print(my_list)

# List operations
# We can perform operations on lists such as concatenation, repetition, membership testing, and iteration.

# Concatenation
# We can concatenate two lists using the + operator.

my_list = [1, 2, 3] + [4, 5, 6]
print(my_list)

# Repetition
# We can repeat a list using the * operator.

my_list = [1, 2, 3] * 3
print(my_list)

# Membership testing
# We can test if an element is in a list using the in operator.

print(1 in my_list)

# Iteration
# We can iterate over a list using a for loop.

for element in my_list:
    print(element)
