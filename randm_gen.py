'''
# calling np.random
import numpy as np
rnd = np.random.rand()
print(rnd)

# calling np.random using a seed
import numpy as np
np.random.seed(123)
rnd = np.random.rand()
print(rnd)
'''

'''
# simulating a coin toss, using a random integer generator
import numpy as np
np.random.seed()
coin = np.random.randint(0, 2)  # Note: Up to but not include 2
if coin % 2 == 0:
    print("AGUILA")
else:
    print("SOL")
'''
