'''

import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
# .iterrows() is the method used to iterate over rows
for label, row in brics.iterrows():
    print(lab)
    print(row)

# Print out only the row for the column "capital"
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for label, row in brics.iterrows():
    print(label + ": " + row["capital"])
'''
# Adding a new column by applying the length function to the country's name column
# Note: Don't do it with a loop (liek above) because it would create a series on every iteration (inneficient)
import pandas as pd
brics = pd.read_csv("brics.csv", index_col=0)
brics["name_length"] = brics["country"].apply(len)
print(brics)
