
'''
# Function written BAU
def raise_to_power(x, y): return x ** y
result = raise_to_power(2, 3)
print(result)

# Written as a Lambda function
# raise_to_power = lambda x, y: x ** y
result = raise_to_power(2, 3)
print(result)

# as an anonymous function
nums=[2, 4, 6, 8, 9]

square_all=map(lambda num: num ** 2, nums)
# square all returns a map object that ...
# needs to be turned into a list for printing
print(list(square_all))
'''
