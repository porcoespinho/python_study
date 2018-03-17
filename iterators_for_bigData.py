'''
# too much data? load it in chunks
# process one chunk and discard it
# then load the next. Perfect use of iterators
# use pandas read_csv(), specify chunks...
# with the argument chunksize

# ---- Example 1 --------
# Add all the numbers in a column
import pandas as pd
# create a list to hold the result
result = []
for chunk in pd.read_csv('data.csv', chunksize=1000):
    # the object created by read_csv is an iterable
    # each iterated-chunk becomes a dataframe
    result.append(sum(chunk['x']))
total = sum(result)
print(total)

# alternative without using a list
import pandas as pd
total = 0
for chunk in pd.read_csv('data.csv', chunksize=1000):
    total += sum(chunk['x'])
print(total)

# ---- Exercise 1 --------
# processing tweeter data 'tweets.csv'
import pandas as pd

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)

# ---- Exercise 2 --------
# processing 'tweets.csv' chunks with a function
# processing tweeter data 'tweets.csv'
import pandas as pd

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)
