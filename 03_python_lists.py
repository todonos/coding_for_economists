# In this file we will look at lists, dictionaries, set, tuples, range.

# List
myList = [1, 2, 3, 4, 5]  #when create list use square brackets
print(myList)

print(type(myList))  # class list

# Grab the first object of list
print(myList[0])  #1

print(myList[-1])  #5

# How many objects does list have?
print(len(myList))  #5
print(f'Our list object myList has {len(myList)} elements')

# Nice thing about lists: they are flexibel with respect to the data type
mixedList = [1, 'two', 3.0, [4, 'four'], 5]
print(mixedList)

# We can also add and remove objects from a list
mixedList.append(6)
print(mixedList)
mixedList.pop()  #if not specify index, it will remove last object
print(mixedList)
mixedList.pop(0)  #if specify index, it will remove object at that index
print(mixedList)

# How many times does the integar 3.0 appear
print(mixedList.count(3.0))

# Reverse a list
mixedList.reverse()
print(mixedList)
