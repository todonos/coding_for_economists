#1. Navigate back to raw/ (<cd ..>)
#2. Create a folder called raw/country-codes (<mkdir>)
#3. Download the country-codes.csv file into country_codes/ (curl -L -o fname url)

url = 'https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv'

#2024.01.16
#Exercise: Indexing and slicing

#Use indexing, slicing to fill in the following output
#copy/ paste is not allowed

file_name = url[-14:]
print(file_name) #ted-sample.csv

protocol = url[0:5]
print(protocol) #https

host_name = url[8:18]
print(host_name) # 'github.com'

#Use string composition to construct http://github.com/ted-sample.csv

all = protocol + '://' + host_name + '/codedthinking/tender-home-bias/releases/download/v1.0/' + file_name