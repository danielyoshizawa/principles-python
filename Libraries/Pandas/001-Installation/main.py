# Installation of Pandas

# Pandas is a library that provides data manipulation and analysis.
# It is built on top of NumPy and provides data structures for efficiently manipulating numerical tables and time series.

# Installation

# pip install pandas

# Importing Pandas

import pandas as pd

# Example

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# Checking pandas version

print(pd.__version__)

# Importing Pandas with alias

