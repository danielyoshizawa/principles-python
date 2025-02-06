# Cleaning Empty Cells

# Empty Cells

# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows

# One way to deal with empty cells is to remove rows that contain empty cells.

# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

# Example

# Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

# NOTE: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument:

df.dropna(inplace = True)

print(df.to_string())

# NOTE: Now, the dorpna(inplace = True) will not return a new DataFrame, but it will change the original DataFrame.

# Replace Empty Values

# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:

# Example

# Replace NULL values with the number 130:

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

print(df.to_string())

# Replace Only For Specified Columns

# The example above replaces all empty cells in the whole Data Frame.

# To only replace emptyh values for one column, specify the column name for the DataFrame:

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True) # Will no longer work on pandas 3.0

print(df.to_string())

# Pandas 3.0 method call to operate inplace, use
# df.method({col: value}, inplace=True)
# df[col] = df[col].method(value) 
# to perform the operation inplace on the original object.

# Replace Using Mean, Median, or Mode

# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Mean = the average value (the sum of all values divides by number of values)
# Example

# Calculate the MEAN, and replace any empty values with it:

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

# Median = the value in the middle, after you have sorted all values
# Example

# Calculate the MEDIAN, and replace any empty values with it:

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

# Mode = the value that appears most frequently 
# Example

# Calculate the MODE, and replace any empty values with it:

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())




