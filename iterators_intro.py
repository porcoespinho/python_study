
'''
# ITERATING OVER LISTS
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for name in flash:
    print(name)


# Create an iterator for flash: superspeed
#...iter() gets us an iterator object
superspeed = iter(flash)

# Print each item from the iterator
#...next() retrieves the iterator's values
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))

# ITERATING OVER A RANGE
# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for i in range(3):
    print(i)

# Iterators as function arguments
# Create a range object: values
values = range(10, 21, 1)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)

'''
