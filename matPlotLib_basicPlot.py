import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
# help(plt.plot)
# add more data
year = [1700, 1760, 1804, 1850, 1927] + year + [2011, 2012, 2013, 2014, 2015, 2016, 2017]
pop = [.610, .770, 1.0, 1.2, 1.6] + pop + [7.043, 7.128, 7.213, 7.298, 7.383, 7.466, 7.550]
plt.plot(year, pop)  # line plot
# plt.scatter(year, pop)  # scatter plot
plt.yticks([0, 2, 4, 6, 8],
           [0, '2b', '4b', '6b', '8b'])
plt.title('world poppulation over time')
plt.xlabel('year')
plt.ylabel('poppulation')
plt.show()
