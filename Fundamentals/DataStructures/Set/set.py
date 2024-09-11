# Set

# Sets are unordered collections of unique elements.
# Sets are created using curly braces {} or the set() constructor.
# Sets are unordered, which means we cannot access elements using indices.
# Sets are mutable, which means we can add, modify, and remove elements from them.

# Set operations
# We can perform set operations such as union, intersection, difference, etc.
# We can use methods such as add, remove, clear, etc.

# Set comprehension
# We can create a new set using a set comprehension.
# The syntax is similar to list comprehension, but we use curly braces {} instead of square brackets [].

my_set = {i for i in range(10)}
print(my_set)

# Set union
# We can use the union method to combine two sets.
# We can use the | operator to combine two sets.

my_set2 = {i for i in range(10, 20)}
print(my_set | my_set2)

# Set intersection
# We can use the intersection method to find the common elements between two sets.
# We can use the & operator to find the common elements between two sets.

my_set3 = {i for i in range(5, 15)}
print(my_set & my_set3)

print(my_set3 & my_set3)

# Set difference
# We can use the difference method to find the elements that are in one set but not in the other.
# We can use the - operator to find the elements that are in one set but not in the other.
print(my_set - my_set3)
print(my_set3 - my_set)

# Set symmetric difference
# We can use the symmetric_difference method to find the elements that are in one set but not in the other.
# We can use the ^ operator to find the elements that are in one set but not in the other.
print(my_set ^ my_set3)

# Example with explicit method call
print(my_set.symmetric_difference(my_set3))

# Explanation
print("Symmetric difference returns elements that are in either set, but not in both.")
print(f"Elements unique to my_set: {my_set - my_set3}")
print(f"Elements unique to my_set3: {my_set3 - my_set}")
print(f"Symmetric difference: {my_set ^ my_set3}")

# Set membership
# We can use the in operator to check if an element is in a set.
# We can use the not in operator to check if an element is not in a set.
# Set membership examples
print("\nSet membership:")
element = 5
print(f"Is {element} in my_set? {element in my_set}")

non_element = 20
print(f"Is {non_element} not in my_set? {non_element not in my_set}")

# Practical example
valid_colors = {"red", "green", "blue"}
user_color = "yellow"
if user_color in valid_colors:
    print(f"{user_color} is a valid color.")
else:
    print(f"{user_color} is not a valid color.")


# We can use the add method to add an element to a set.
# We can use the remove method to remove an element from a set.
# We can use the clear method to remove all elements from a set.
# We can use the discard method to remove an element from a set if it exists.

# Adding elements to a set
print("\nAdding elements to a set:")
colors = {"red", "green", "blue"}
print(f"Original set: {colors}")

colors.add("yellow")
print(f"After adding 'yellow': {colors}")

# Removing elements from a set
print("\nRemoving elements from a set:")
print(f"Current set: {colors}")

colors.remove("green")
print(f"After removing 'green': {colors}")

# Using discard method
print("\nUsing discard method:")
print(f"Current set: {colors}")

colors.discard("blue")
print(f"After discarding 'blue': {colors}")

colors.discard("purple")  # This won't raise an error if 'purple' doesn't exist
print(f"After discarding 'purple' (which wasn't in the set): {colors}")

# Clearing a set
print("\nClearing a set:")
print(f"Current set: {colors}")

colors.clear()
print(f"After clearing the set: {colors}")

# Demonstrating the difference between remove and discard
print("\nDifference between remove and discard:")
numbers = {1, 2, 3, 4, 5}
print(f"Original set: {numbers}")

numbers.discard(6)  # This won't raise an error
print(f"After discarding 6 (which wasn't in the set): {numbers}")

try:
    numbers.remove(6)  # This will raise a KeyError
except KeyError:
    print("Trying to remove 6 raised a KeyError because it's not in the set")

print(f"Final set: {numbers}")
