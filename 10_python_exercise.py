# EXERCISE 3

# In this exercise we want to count the number of times each country won a tender in the ted-sample.csv file

# 1: Find the index position of the column "WIN_COUNTRY_CODE"
# Hint: Grab the header and assign them to a variable. Then, iterate through headers using enumerate()
f = open('data/raw/european_commission/ted-sample.csv',
         'r')  #'r' is default mode
# grab headers
headers = f.readline().strip().split(',')

# make sure to close the file
f.close()

for index, value in enumerate(headers):
  print(index, value)  # 61 WIN_COUNTRY_CODE

# ажиглалт бүрээс 61 дэх мэдээллийг хайж улсын тоогоор тоолно

# 2: Instantiate an empty list called data
data = []

# 3: Iterate through the line of the csv file using the context manager open() and append the observation as a list.
# 3.1: iterate through each row in ted-sample.csv and
# 3.2: append each row to the data list using (in the loop body) data.append(list(line.split(",")))

with open('data/raw/european_commission/ted-sample.csv', 'r') as f:
  for line in f:
    data.append(list(line.split(",")))

print(data[0])

# output should look like: [[row0], [row1], ..., [rowN]] list of list

data = data[1:]  # remove the header
#or we can use data.pop(0)

# 4. Count the number of wins by country
win_country = {}
for row in data:
  if not row[61] in win_country:
    win_country[row[61]] = 0
  win_country[row[61]] += 1

print(win_country)

# another solutions
win_country1 = {}
for row in data:
  country = row[61] #careful: some tenders are won by more than one country
  countries = country.split('---') # Returns a list of winning countries
  for winning_country in countries:
    if not winning_country in win_country1:
      win_country1[winning_country] = 0
    win_country1[winning_country] += 1

print(win_country1)

# Hint: Use the .split() method on the line to automatically create a list, passing the appropraite argument to split.
# Hint: 'a, b, c.split(",")' = ['a', 'b', 'c']'

# Example of count in list
a = [1, 2, 4, 1, 2, 1]
d = {}
for num in a:
  if not num in d:
    d[num] = 0
  d[num] += 1

print(d)
