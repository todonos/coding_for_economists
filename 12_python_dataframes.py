# Intro do pandas.DataFrames
import pandas as pd
import numpy as np

# Create some raw data to construct df
data = {'Tokyo': 30_000_000, 'Delhi': 50_000_000, 'Shanghai': 20_000_000}

# Create df from dict
df = pd.DataFrame(data, index=[0])
print(df)

# Create a df drom csv
df_raw = pd.read_csv('https://osf.io/yzntm/download')

# Inspect
print(df_raw.head())

# Waht are the dimensions of our data?
print(df_raw.shape)

# Access number of rows
print(df_raw.shape[0])

# Name of columns
print(df_raw.columns)

# Create new column: multiple ways of doing so
# df.nnights = 1
# df['nnights'] = 1
df = df_raw.assign(nnights=1)

# Delete df_raw since we do not need it anymore
del df_raw

# Let's check out accomodation type variable
df['accommodationtype'].head()

# We want to clean this up
df['accommodationtype'] = df['accomodationtype'].str.split('@').str[1]

# How many nights in each accommodation type?
df['accommodationtype'].value_counts()

 # Clean up missing value / if there is missing or empty you can replace it
df.accommodationtype.replace('', 'Unknown', inplace=True)

# Look at guestreviewrating
df['guestreviewrating'].head()

# Create clean variable for ratings
df['ratings'] = df['guestreviewsrating'].str.split('/').str.strip()

# Convert to float
df['ratings'] = df['ratings'].astype(float)

#What is the average rating?
print(df['ratings'].mean())

# Small exercise: There's a variable called center1distance. What is the average distance to the center?
# Need to split at whitespace
df['distance_numeric'] = df['center1distance'].str.split(' ').str[0]

df.distance_numeric
df.distance_numeric = df.distance_numeric.str[0]

df['distance_numeric'] = df ['distance_numeric'].astype(float)]
df.distance_numeric.dtype
df.columns

# There are a few rating related variables: let's inspect them
df.filter(regex = 'rating')
df.filter(regex = 'rating').head()

# Renaming variable
df.rename(columns = {'rating_reviewcount': 'ratings_count', 'rating2_ta': 'ratingta'}, inplace = True)

# Exercise: rename the following variables:
# ratings2_ta_reviewcount: ratingta_count
#addresscountrytype: country 
# starrating: stars
# s_city: city

# Subsetting dataframe
df.loc[df['accommodationtype''] == 'Hotel']

print(df.loc[df['accommodationtype'] == 'Hotel'])

# How to check for missing values?
print(df.ratings.isnull().sum())

# Count missing values by certain group
print(df.ratings.isnull().groupby(df.country).sum().value_counts())