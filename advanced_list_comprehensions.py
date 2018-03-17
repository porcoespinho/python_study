'''
Note: LC abbreviates 'list comprehension'

# Conditionals on the LC iterable
cond_square = [num**2 for num in range(10) if num % 2 == 0]
print(cond_square)

# Conditionals on the output expression
cond_square2 = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(cond_square2)

# Dictionary comprehensions (DC)
# With DC we use iterables to create dictionaries
# Two main differences between DC and LC:
# (1) We use {} instead of []
# (2) Key and value are separated by : in the output

# DC example 1
pos_neg = {num: -num for num in range(4)}
print(pos_neg)
# output => {0: 0, 1: -1, 2: -2, 3: -3}

# Conditional LC, exercise 1
# conditional in the iterator (predicate expression)
# Keep strings with 7 characters or more.
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)

# Conditional LC, exercise 2
# If-Else in the output expression
# Keep strings with 7 characters or more...
#...replaces others with ''.
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)

# Dictionary comprehension, exercise 3
# create a dictionary with list-members as keys
# and the string length as values.

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new list
print(new_fellowship)

# -----------------

Exercise: Conditional list comprehesions for time-stamped data

import pandas as pd
df = pd.import(''tweets.csv'')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the time stamp pos 12 to 19 : tweet_clock_time
# Select the times in which entry[17:19] is equal to '19'
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']


# Print the extracted times
print(tweet_clock_time)

# -----------------

# Exercise: use a function in a list comprehension...
#...to generate a list of dictionaries. Convert the
#...list of dictionaries into a pandas DataFrame.

# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())


# Exercise: Writing an iterator to load data in chunks (2)

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize = 1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)

'''
