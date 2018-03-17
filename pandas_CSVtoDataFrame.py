# Import pandas as pd
import pandas as pd

# Import using the path and including the first column as index
naturalized = pd.read_csv('/Users/lvargas/Downloads/Persons Naturalized By Region And Country Of Birth - Sheet1.csv', index_col=0)

# Print it out
# print(naturalized)

'''
# Select the 2014 column by using single [] but it returns a pandas.core.series
year_2014 = naturalized["2014"]
print(year_2014)
print(type(year_2014))

# Select the 2016 column by using double [[]] to get the column in a data frame
year_2016 = naturalized[["2015", "2016"]]
print(year_2016)
print(type(year_2016))

# It's easy to add another year with a comma inside the [[]]
two_years = naturalized[["2015", "2016"]]
print(two_years)
print(type(two_years))

# Slice rows 1-3 by number (index 0 and does NOT include the last column)
first_three = naturalized[0:4]
print(first_three)


# Use loc to select data based on  labels OR you can also use iloc to select  based on index position

# topThree = naturalized.loc[["Afghanistan", "Albania", "Algeria"]]
# OR
topThree = naturalized.iloc[[1, 2, 3]]
print(topThree)
print(type(topThree))


# Use loc to select data based on row AND column labels OR you can also use iloc to select  based on index position
topThree_201516 = naturalized.iloc[[1, 2, 3], ] , ["2015", '2016']]
# OR top
topThree_201516 = naturalized.iloc[[1, 2, 3], [1, 2]]
print(topThree)

# Use loc to select data based on row AND column labels (use : to select all rows)
twentysixteen = naturalized.loc[:, ["2016"]]
print(twentysixteen)
'''
