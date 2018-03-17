'''
# IMPORTING TEXT FILES LINE BY LINE

# Open the file as read-only and store it in: file
file = open('moby_dick.txt', mode = 'r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)


# Close file
file.close()

# Check whether file is closed
print(file.closed)

# IMPORTING TEXT FILES LINE BY LINE

# bind a variable file with a context manager:
with open('moby_dick.txt') as file:
    # Print the first 3 lines
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Ex 1: Importing flat files using numpy
# if all data is numerical import as numpy array

import numpy as np
filename = 'MNIST.txt'
data = np.loadtxt(filename, delimiter=',')

# skip 1st line if it contains headers
data = np.loadtxt(filename, delimiter=',', skiprows=1)

# if you want only the 1st and 3rd column of the data
data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0, 2])

#  importing strings int numpy
data = np.loadtxt(filename, delimiter=',', dtype=str)

# .loadtxt() tends to fail with mixed data types

# Ex 2: Importing flat files using numpy
# Import package
import numpy as np

# Assign filename to variable: file
file = 'digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=",")

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

# CUSTOMIZING YOUR NUMPY IMPORT

# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: tab-delimited, skip one row, only 1st & 3rd columns.
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

# Print data
print(data)

# IMPORTING DIFFERENT DATATYPES
# the file's text header of consists of strings
# skip row 1 to avooid a ValueError 'could not convert string to float'

# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()


# 'WORKING WITH MIXED DATATYPES (A)'
# for datasets with different datatypes (i.e. one column strings, another floats) use np.loadtxt()
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)
# the argument 'names' tells us there is a header
# with'dtype=None' Numpy will figure  what type each column should be
# each element of the resulting array is a row of the flat file imported


# 'WORKING WITH MIXED DATATYPES (A)'
# np.recfromcsv() has the defaults:
# delimiter=',' & names=True & dtype=None!

# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])

# 'BEST PRACTICE: IMPORT FLAT FILES INTO DATAFRAMES'
# 'USING PANDAS TO IMPORT FLAT FILES AS DATAFRAMES'

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

# NUMPY ARRAY FROM A DATAFRAME USING "VALUES"

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'digits.csv'

# Import file's first 5 rows (no header) into a DataFrame: data
data = pd.read_csv(file, nrows = 5, header = None)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))

# COMMON ISSUES: COMMENTS, MISSING VALUES, OTHER DELIMITERS

# sep the pandas version of delim),
# comment takes characters that precede a comment in the file
# na_values  takes strings to recognize as NA/

# Import pandas as pd
import pandas as pd

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep=____, comment=____, na_values=____)

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

# EXPLORE YOUR CURRENT WORKING DIRECTORY
# import the library os
import os
# store name of current directory in wd
wd = os.getcwd()
# outputs directory contents in a list
print(os.listdir(wd))

# IMPORTING OTHER FILE TYPES

# Loading a pickled file
# Import pickle package
import pickle

# Open pickle file and load data: d
# read only for a binary file
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

# Listing Excel file's sheets' names
# import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

# Importing sheets from Excel files
# import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

# 'CUSTOMIZING YOUR SPREADSHEET IMPORT'
# import pandas
import pandas as pd

# Assign spreadsheet filename: file
xl = 'battledeath.xlsx'

# Load the 1st sheet and uinto a dataframe, rename columns
df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Load the 1st column of the 2nd sheet, rename the column
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

# IMPORTING SAS FILES

# import pandas
import pandas as pd

# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# 'sales.sas7bdat' is  in your working directory

# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print the head of the DataFrame df_sas
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()


# 'IMPORTING STATA FILES'

# Import pandas
import pandas as pd

# 'disarea.dta', is in your working directory

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()


# 'USING FILE TO IMPORT HDF5 FILES'

# import numpy as np
import numpy as np

# the h5py package has been imported
import h5py

The file 'LIGO_data.hdf5' is in your working directory

# Assign filename: file
file = 'IGO_data.hdf5'

# import the file as an object as read -nly
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)



# 'EXTRACTING DATA FROM YOUR HDF5 FILE'

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
'''
