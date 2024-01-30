# Introduction to pandas and numpy
# Pandas is a python library for data manipulation
import pandas as pd
import numpy as np

# pip is the package install pandas
# pip install pandas
# work in shell (python)
import numpy as np
import pandas as pd

# Let's look at pd.Series
# A series is a one-dimensional array like object

# Let's define our first pd.Series
# Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
ps = pd.Series(['a', 1, 3, np.pi])
print(ps)

# Which data type does our pd.Series have?
print(type(ps))  #pandas.core.series.Series

# We can access the values
print(ps.values)
print(type(ps.values))  #numpy.ndarray

# We can access the index
print(ps.index

# Access elements of pd.Series by indexing
print(ps[0])
print(ps[0:2])

# Define a custom index
series_1 = pd.Series(
  data = ['Schnitzel',
         'Lemonade',
         'Whiskey'],
  index = ['food', 
           'soda', 
           'alcohol']
)

# Advanced indexing of pd.Series
# using .loc[]
print(series_1.loc['food'])

# Accessing more than single index
print(series_1.loc[['food', 'soda']])

# using .iloc[]
series_1.iloc[0]

# Access elements from a range of indexes
series_1.loc['food' : 'soda']