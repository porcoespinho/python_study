''' Abbreviations:
Generators = G, list comprehensions = LC...
Dictionary comprehensions = DC.
For G Use (), for LC [], for DC {}
What do each return? LC a list, G a generator object..
...DC a dictionary. All can be iterated over.

Generators do not store the output in memory...
they just return an object we can iterate on..
...to create list elements as required.

'Lazy Evaluation': The evaluation of the expression...
... is delayed until the value is needed.

# G Example 1: Print through iteration
result = (num for num in range(6))
for num in result:
    print(num)

# G Example 1a: Print as a list
result = (num for num in range(6))
print(list(result))

# G Example 2: Conditionals in G expressions
even_nums = (num for num in range(10) if num % 2 == 0)
print(list(even_nums))

# Generator function, example 1:
# G functions use the keyword YIELD...
# instead of the keyword RETURN ...
# ... like a regular function.

def num_sequence(n):
    """ generates values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

# Use a generator(G) function
result = num_sequence(5)
for item in result:
    print(item)

# Generator function, example 2:

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
# Create a list of strings

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
for value in get_lengths(lannister):
    print(value)

# Generator function, Exercise 1:
# Processing big data in chunks
# Using the World Development Indicators (WDI) dataset
# create a dictionary of the counts of...
# ... # of times a country appears in the dataset.


# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))


# Exercise 3: Now process the whole dataset...
# using the generator function above
#

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print
print(counts_dict)

# Exercise: read the file in as DataFrames...
# of a certain length, say, 10
# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize = 10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))
'''
