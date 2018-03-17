# Example: Setting a default argument
def power(number, pow=1):
    # above, 1 is the default argument for the second parameter
    """Raise number to the power of pow."""
    new_value = number ** pow
    return new_value


print(power(3))  # results in 3, because of the default value


# Example: Flexible arguments
def add_all(*args):
    """ Sums all values in *args together. """
    # note *args turns all arguments passed into a tuple called args

    # Initialize sum
    sum_all = 0

    # Accumulate the sum
    for num in args:
        sum_all += num

    return sum_all


print(add_all(1, 2, 4))


# Example: Keyword arguments (**kwargs)

def print_all(**kwargs):
    """Print out key-value pairs in **kwargs."""
    for key, value in kwargs.items():
        print(key + ": " + value)

    # Note: **kwargs turns the identifier-keyword pairs...
    #...into a dictionary within the function body

    # Print out the key-value pairs
print_all(name="Luis Vargas", employer="Netflix")
