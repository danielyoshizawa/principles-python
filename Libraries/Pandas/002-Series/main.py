# Series

# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# Example
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# Labels

# If nothing else is specified, the values are labeled with their index number.
# First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.

# Example

print(myvar[0]) # Accessing the first value by index

# Example

print(myvar[1]) # Accessing the second value by index

# Create labels

# With the index argument, you can name your own labels.

# Example

myvar = pd.Series(a, index = ["x", "y", "z"])

# Printing by label
print(myvar["y"])

# Key/Value Objects as Series

# You can also use a key/value object, like a dictionary, when creating a Series.

# Example

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# Note: The keys of the dictionary become the labels.

# To select only some of the items in the dictionary, use the index argument and
# specify only the items you want to include in the Series.

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

# DataFrames

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
# Series is like a column, and DataFrame is the whole table.

# Example

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
