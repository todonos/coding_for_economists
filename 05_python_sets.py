# Intro to data type set

# Set is a collection of well defined objects
mySet = {1, 2, 3, 4, 5}
print(mySet)

#Check type
print(type(mySet))

# Sets only contain uniquie values
mySet = {1, 2, 3, 4, 5, 5} #duplicate 5  
print(mySet)

# Check membership
print(1 in mySet)

print(set("aaaaaabbbbbbcccc"))

# Define two sets and check our set operations
setA = {1, 2, 3, 4, 5}
listB = [3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,]
setB = set(listB)

print(setA, setB)

# Set union
unionAB = setA | setB
print(unionAB)

# Set intersection
intersectionAB = setA & setB
print(intersectionAB)