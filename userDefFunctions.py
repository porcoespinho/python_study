
'''
# Write a simple function with a single-parameter

def shout(word):
    """Print a string with three exclamation marks"""
    shout_word = word + '!!!'
    return shout_word


yell = shout('GIVE ME FIVE')
print(yell)

# unpacking tuples
tup = (1, 2, 3)
a, b, c = tup
print(c)

def raise_both(value1, value2):
    """ Return value1 to the power of value2 and viceversa """
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1

    new_tuple = (new_value1, new_value2)
    return new_tuple


result1, result2 = raise_both(4, 2)  # here we assign new_tuple
print(result1)
print(result2)
'''
