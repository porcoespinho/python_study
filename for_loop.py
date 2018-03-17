'''
for c in "family":
    print(c.capitalize())

# Nested for loop
a = [[1, 3, 4], [2, 4, 4], [3, 4, 5]]
for list in a:
    for number in list:
        print(number)
output
1
3
4
...etc

# Build a for loop from scratch
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

for l in house:
    print("the " + l[0] + " is " + str(l[1]) + " sqm")

# iterating over a dictionary with a for loop
world = {"afghanistan": 30.55, "albania": 2.77,
         "algeria": 39.21}
for key, value in world.items():
    print(key + " " + str(value))

# iterating over a one-dimensional numpy array with a for loop
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
for val in bmi:
    print(val)
'''
# Using numpy.nditer object to iterate over an n-dimensional arrays
import numpy as np
np_ht = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_wt = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_ht, np_wt])
for val in np.nditer(meas):
    print(val)
