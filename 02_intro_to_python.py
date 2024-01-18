# Basic arithmetic opeartion in python

# Adding two numbers
print(2 + 3)
2 + 3  #not show result

# Divide two numbers
print(10 / 5)

# Careful division returns a float
print(type(10 / 5))  # class float

# You can't specify float or intiger in python

# Exponentiation
print(2**3)

# Assigning variables
x = 5
y = x**2
print(y)

# String
a = "Hello, how're you?"  # equivalently: use one or two quotation marks '' ""

# Arithmetic operations on strings
# Multiplication
print(a * 3)

# Concatenation
b = "I'm good, thank you"
print(a + " " + b)

# Substraction
# print(a - b)  # error

# # Error message includes file name, line and type of error (just show you first error)

# # Division
# print(a / b)  # error

# Shortcut of commented code: ctrl + /

# Indexing and slicing
# First element
print(a[0])

# Last element
print(a[-1])

# Slicing
print(a[0:5])

# How many characters does our string have?
print(len(a))
print(f'Our string has {len(a)} characters')
print("Our string has {} characters".format(len(a)))

# Have a look at logical statements
print(2 == 2)  # True (equivalent to 1)
print(2 == 3)  # False (equivalent to 0)

# Check if True and 1 are in facr equivalent
print(True == 1)
print(type(True))  # class bool
print(type(1))  # class int

# Boolen operators will used for gender also

# Check equivalence of two variables
print(a == b)

# Multiple logical statements
print(2 == 2
      and 3 == 3)  # if you use "and" operator, both statements must be true
print(2 == 2 and 3 == 4)

print(2 == 2
      or 3 == 4)  # if you use "or" operator, only one statement must be true
print(2 == 3 or 3 == 4)
