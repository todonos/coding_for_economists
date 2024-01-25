# Read text files

# Open
file = open('data/raw/european_commission/ted-sample.csv')  #check directory

print(file.readline())  #print 1st line
print(file.readline())  #print 2nd line

file.close()

# Here we have to close the file manually, not ideal.

# Context manager
with open('data/raw/european_commission/ted-sample.csv') as file:
  for line in file:
    print(line)  #ctrl + C to stop it is not work for my laptop
