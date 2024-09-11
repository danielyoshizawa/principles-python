#Dictionary

# Dictionaries are unordered collections of key-value pairs.
# They are mutable, which means we can add, modify, and remove elements from them.
# Dictionaries are indexed by keys, which can be any immutable type such as strings, numbers, or tuples.
# Dictionaries are created using curly braces {} or the dict() constructor.

my_dict = {"name": "John", "age": 25, "city": "New York"}

# Accessing elements
print(my_dict["name"])

# Adding elements
my_dict["occupation"] = "Software Engineer"
print(my_dict)

# Removing elements
del my_dict["city"]
print(my_dict)

# Dictionary methods
# We can use methods to perform operations on dictionaries.
# Some of the methods are get, keys, values, items, etc.

# get
print(my_dict.get("name"))

# keys
print(my_dict.keys())

# values
print(my_dict.values())

# items
print(my_dict.items())

# Iterating over a dictionary
for key, value in my_dict.items():
    print(key, value)

# Dictionary comprehension
# We can create a new dictionary using a dictionary comprehension.
# The syntax is similar to list comprehension, but we use curly braces {} instead of square brackets [].

my_dict = {i: i * 2 for i in range(5)}
print(my_dict)

# Dictionary comprehension with condition
my_dict = {i: i * 2 for i in range(5) if i % 2 == 0}
print(my_dict)
