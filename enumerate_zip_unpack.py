# enumerate() adds a counter to any iterable...
# ...it takes an iterable as argument
#... returns an object iterable's args with an index
'''
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)

# print(type(e))  # <class 'enumerate'>
e_list = list(e)  # turn into a list of tuples
print(e_list)
#...[(0, 'hawkeye'), (1, 'iron man'), ...]

# the enumerate object is also an iterable...
# and we can loop over it...
for index, value in e:
    print(index, value)
    # 0 hawkeye
    # 1 iron man
    # 2 thor...etc

# changing the start index of enumerate
for index, value in enumerate(avengers, start=10):
    print(index, value)
    # 10 hawkeye
    # 11 iron man
    # 12 thor...etc
'''
# --------------------------------
'''
# zip() accepts any number of iterables...
#... returns an iterator of tuples matching the lists
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)  # turn into an iterator of tuples
# print(type(z))
# <class 'zip'>

z_list = list(z)
print(z_list)
# [('hawkeye', 'barton'), ('iron man', 'stark'), ...etc]

# Alternative using a for loop
for z1, z2 in zip(avengers, names):
    print(z1, z2)

# the output looks like...
# hawkeye barton
# iron man stark
# ...etc


# Alternative using the splat operator
print(*z)
# the output looks like...
# ('hawkeye', 'barton') ('iron man', 'stark') ...etc

---- Exercise 1 ----
# Using Enumerate
# Create a list of strings: mutants
mutants = ['charles xavier',
            'bobby drake',
            'kurt wagner',
            'max eisenhardt',
            'kitty pride']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in mutant_list:
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start = 1):
    print(index2, value2)

---- Exercise 2 ----
# using zip()

mutants = ['charles xavier',
 'bobby drake',
 'kurt wagner',
 'max eisenhardt',
 'kitty pride']

aliases ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']

powers = ['telepathy',
 'thermokinesis',
 'teleportation',
 'magnetokinesis',
 'intangibility']

 # Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

---- Exercise 3 ----
# 'unzip' tuples produced by zip() with *zip()
'''
mutants = ('charles xavier',
           'bobby drake',
           'kurt wagner',
           'max eisenhardt',
           'kitty pride')

powers = ('telepathy',
          'thermokinesis',
          'teleportation',
          'magnetokinesis',
          'intangibility')

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = *zip(z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)
