# introduce packages
import random

# generate random interger between 20 and 34
random_number = random.randint(20, 34)
print(random_number) #we get a different random integer each time we run the script

# first look at conditional statements
# cases should be tupically be exhausted

if random_number < 25:
  print('The number is less than 25')
elif random_number < 30:
  print('The number is less than 30')
else:
  print('The number is less than 34') #if first condition met, python does not execute next line

# nested if statement
a = random.randint(0, 10)
b = random.randint(10, 20)

if a < 9:
  print(f'a is less than 9.')
  if b< 19:
    print(f'b is smaller than 19')

# Equivalently, we can combine the logical conditions
if a < 9 and b < 19:
  print('a is less than 9 and b is less than 19')
  