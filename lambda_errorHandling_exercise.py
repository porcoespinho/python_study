'''
# EXERCISE 1: SELECT RETWEETS

# Import tweeter data into the DataFrame, tweets_df
import pandas as pd
tweets_df = pd.read_csv('tweets.csv')

# Select retweets from the twitter dataframe
# (1) Convert the tweets_df into text
# (2) Check if the first 2 characters in a tweet x are 'RT' (i.e. retweet).
result = filter(lambda x: x[0, 2] == 'RT', tweets_df['text'])

# Create a list from the filter object
res_list = list(result)

# Print all retweets in res_list
print(res_list)

# ---------------

# EXERCISE 2: COUNT ENTRIES FOR A GIVEN DATAFRAME COLUMN

# Import tweeter data into the DataFrame, tweets_df
import pandas as pd
tweets_df = pd.read_csv('tweets.csv')

# Define the function count_entries()

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
        cols_count = {}

        # Add try block
        try:
            # Extract column from DataFrame
            col = df[col_name]

            # Iterate over the column in dataframe
            for entry in col:

                # If entry is in cols_count, add 1
                if entry in cols_count.keys():
                    cols_count[entry] += 1
                    # Else add the entry to the dictionary with value 1
                else:
                    cols_count[entry] = 1

            # Return the cols_count dictionary
            return cols_count

            # Add except block
            except:
                # Print error message
                print('The DataFrame does not have a ' + col_name + ' column.')

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang1')

# ---------------
'''
# EXERCISE 3: Raise a ValueError if the user provided column name  isn't in the DataFrame.



