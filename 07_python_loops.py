# let's have a look at loop syntax

# for loop operates on 'iterable'

# let's create an iterable object
myList = [1, 2, 'abc']

# let's iterate over the object
for item in myList:
  # loop body needs to be intended once
  print(item)

for banana in myList:
  if banana == 1:
    print(banana)
  else:
    print('item not equal to 1.')

# looping over a range of values
for i in range(5): #range() generates value on the fly
  print(i)

# another way to do it
range_vals = [0, 1, 2, 3, 4] #not memory efficient
print('Using a list to display values 0-4')
for i in range_vals:
  print(i)

a = range(5)
print(a)
type(a) #class range

# looping over list of strings and nesting loops
for name in ['Alice', 'Bob', 'Charlie']:
  print(name)
  for letter in name:
    print(letter)

# using the enumerate() function to get both index and value
print('Using enumerate()')
for index, name in enumerate(['Alice', 'Bob', 'Charlie']):
  print(index, name)

# equivalent loop using indexing
print('Using range() and indexing')
myList = ['Alice', 'Bob', 'Charlie']
for index in range(len(myList)): #range 3
  print(index, myList[index])

# Use a loop to create a list of capital letters A-Z
print('Using a loop to create a list of capital letters A-Z')
#unicode all signs and letters coded in someway
#example
print(chr(65)) #A in unicode
alphabet = []
for i in range(65, 91): #65-90
  print(i, chr(i))
  alphabet.append(chr(i))
print(alphabet)

# Use a loop to create a list of lowercase letters a-z
print('Using a loop to create a list of lowercase letters a-z')
lower_case = []
for i in range(97, 123):
  lower_case.append(chr(i))
print(lower_case)

# while loop
# while loops are used when you don't know how many times you need to iterate
# instantiate counter variable
i = 0
while i < 10:
  print(i)
  # increment counter every iteration, otherwise it will loop forever
  i += 1
# while gd bichsen nuhtsul biyelehgui boltol iteration ajillana

# List comprehesion
# let's have a look at a for loop creating a list of squares from 0 to 10

squares = []
for num in range(0, 11):
  squares.append(num**2)
print(squares)

# doing the same using list comprehension
squares = [num**2 for num in range(0, 11)]
print(squares)

# using if statement in list comprehension
even_squares = [num**2 for num in range(0, 11) if num % 2 == 0] #even number def (num % 2 == 0) gedeg ni uldegdel ni 0 bh gedgiig tomiyolson
print(even_squares)
