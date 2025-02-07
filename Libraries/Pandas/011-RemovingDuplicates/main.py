# Removing Duplicates

# Discovering Duplicates

# Duplicate rows are rows that have been registered more than one time.

#   11        60  '2020/12/12'    100       120     250.7
#   12        60  '2020/12/12'    100       120     250.7

# By taking a loook at our test data set, we can assume that row 11 and 12 are duplicates.

# To discover duplicates, we can use the duplicated()  method.

# The duplicated() method returns a Boolean value for each row:

# Example

# Returns True for every row that is a duplicate, otherwise False:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())

# Removing Duplicates

# To remove duplicates, use the drop_duplicates() method.

# Example

# Remove all duplicates:

df.drop_duplicates(inplace=True)

print(df.to_string())

# Remember: The (inplace=True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates
# from the original DataFrame.

# Validating the solution

print(df.duplicated())
