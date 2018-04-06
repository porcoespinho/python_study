# "IMPORTING FLAT FILES FROM THE WEB"
'''
# EXERCISE 1:
# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())

# EXERCISE 2: OPENING AND READING FLAT FILES FROM THE WEB'
# Import packages
import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep = ';')

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

# EXERCISE 3: "IMPORTING NON-FLAT FILES FROM THE WEB"
# Import Excel files from the web
# Import package
import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xl
xl = pd.read_excel(url, sheetname = None)

# Print the sheetnames to the shell
print(xl.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xl['1700'].head())

# "GET REQUESTS USING: urllib"

# Example 1: Reading html from Wikipedia
# a) Import the necessary functions
from urllib.request import urlopen, Request
# b) Specify the URL
url = "https://www.wikipedia.org/"
# c) Send the GET request, using 'Request'
request = Request(url)
# d) Catch the response using urlopen
response = urlopen(request)
# e) Use the read method of the HTTPResponse object
html = response.read()
# f) Be polite, close the response
response.close()

# Example 2: Reading html using the requests package
# a) Import requests
import requests
# b) Specify the URL
url = "https://www.wikipedia.org/"
# c) GET, catch, read in one function
r = requests.get(url)
# d) Apply the text method to convert into a string
text = r.text

# Exercise 1:  HTTP REQUESTS USING urllib
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()

# Exercise 2: PRINTING HTTP REQUEST RESULTS USING urllib
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Exercise 4: HTTP REQUESTS USING REQUESTS
# Import package
import requests

# Specify the url: url
url = 'http://www.datacamp.com/teach/documentation'

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)
'''
