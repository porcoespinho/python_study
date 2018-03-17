import numpy as np
# np.random.type of distribution(mean, std deviation, number of samples)
height = np.round(np.random.normal(1.75, 0.20, 25), 2)
weight = np.round(np.random.normal(60.32, 15, 25), 2)
np_city = np.column_stack((height, weight))
print(np_city);
