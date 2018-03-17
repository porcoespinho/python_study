def raise_val(n):
    ''' return the inner function '''

    def inner(x):
        ''' raise x to the power of n. '''
        raised = x ** n
        return raised

    # returns a function
    return inner


# using closure, raise_val returns a function that squares any number
square = raise_val(2)

# using closure,  raise_val returns a function that cubes any number
cube = raise_val(3)


print(square(3), cube(3))

# another example...

# Define three_shouts


def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))


# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))
