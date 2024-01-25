# Lets talk about functions


# Function definition syntax
# def function_name(parameters):
def add_one(num):
  return num + 1


print(add_one(5))


#Function without return statement and without arguments
def add_one_str():
  print(6)


print(add_one_str())

# Try to assign to output of a function to a variable
res = add_one(5)
res_str = add_one_str()

print(res, res_str)


# Multiple return values
def add_one_and_both(num1):
  return num1, num1 + 1


print(add_one_and_both(5))
print(type(add_one_and_both(5)))


# More than one argument in function
def add_two_nums(num1, num2):
  res = num1 + num2
  return num1, num2, res


print(add_two_nums(6, 7))


# Default values for function arguments
def exponentiate(num, exponent=2):
  return num**exponent


print(exponentiate(5, 2) == exponentiate(5))

# Keyword arguments: using the argument name to assign a value: here, order does not matter
print(exponentiate(exponent=1, num=2))


# Function with variable number of arguments
def add_nums(*nums):
  res = 0

  for num in nums:
    res += num
  return res


print(add_nums(1, 2, 3, 4, 5))

# docstrings


# Let's try to code up some docstrings for a functions
def cast_listitems_to_string(list_of_objects):
  """
  Casts all items in a list to string

  Parameters:
  -----------------
  list_of_objects: list

  Returns:
  -----------------
  list_of_strings: list
  """
  list_of_strings = []

  for element in list_of_objects:
    list_of_strings.append(str(element))

  return list_of_strings


print(cast_listitems_to_string([1, 2, '3']))

print(help(cast_listitems_to_string))

# list_of_strings нь зөвхөн функц дотор байгаа скоп буюу функцээс гадна уншуулахад олдохгүй


# Scope of a variable
def test(a, b):
  c = a + b  # Scope of 'c' is confined to function test
  # 'c' is said to have local scope


c = 5  # Here, 'c' is a global scope


# Lambda functions (aka anonymous functions))
# Reference function
def square(x):
  """
  Returns the square of x

  Parameters:
  -----------------
  x: int or float or double

  Returns:
  -----------------
  square_x: int or float or double
  """
  return x**2


# Equivalent lambda function
square_lambda = lambda x: x**2

# Compare results
print(square(7) == square_lambda(7))
