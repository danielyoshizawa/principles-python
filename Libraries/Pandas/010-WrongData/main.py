# Fixing Wrong Data

# "Wrong data" doe not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered
# "199" instead of "1.99"

# Sometimes you can spoot wrong data by looking at the data set, because you have an expectation of what if should be.

# If you take a look at our data set, you can see that in row 7, the duratino is 450, but for all the other rows the
# duratino is between 30 and 60.

# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions,
# we conclude with the fact that this person did not work out in 450 minutes.

# How can we fix wrong values, like the one from "Duration" in row 7?

# Replacing Values

# One way to fix wrong values is to replace them with something else.

# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could
# just insert "45" in row 7.

# Example

# Set "Duration" = 45 in row 7:

import pandas as pd

df = pd.read_csv("data.csv")

df.loc[7, 'Duration'] = 45

print(df.to_string())

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.

# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, 
# and replace any values that are outside of the boundaries.

# Example

# Looop though all values in the "Duration" column.

# If the value is higher than 120, set it to 120:

df.loc[10, 'Duration'] = 121 # To validate the solution

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
        
print(df.to_string())

# Removing Rows

# Another way ofo handling wrong data is to remove the rows that contains wrong data.

# This way you do not have to find out what to replace them with, and there is a good chance you do not need
# them too doo you analyses.

# Example

# Delete rows where "Duration" is higher than 120:

df.loc[10, 'Duration'] = 121 # To validate the solution

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
        
print(df.to_string())