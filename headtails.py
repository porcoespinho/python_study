'''
# 10 random tosses
import numpy as np
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)

# random toss tracking and plotting 'tails' outcomes
import numpy as np
np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot tails
plt.plot(tails)

# Show the plot
plt.show()

# random toss printing every 10th outcome of 100 tosses
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
tenthToss_tails = []
for x in range(1000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    tenthToss_tails.append(tails[-1])
# print(tenthToss_tails)
plt.hist(tenthToss_tails, bins=10)
plt.show()

'''
