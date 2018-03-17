'''
# List comprehensions (LC)
# LC collapse loops for building lists in a single line
# LC components:
    (1)iterable
    (2)iterator variable: represents iterable's members
    (3)output expression

# Ex 1: LC to add 1 to a list
nums = [12, 8, 21, 3, 16]
new_nums = [num + 10 for num in nums]
print(new_nums)

# LC is more efficient than a for-loop
nums = [12, 8, 21, 3, 16]
new_nums1 = []
for num in nums:
    new_nums1.append(num + 10)
print(new_nums1)

# LC work on any iterable,
# Ex 2: LC on a range
# Create list comprehension: squares
squares = [i**2 for i in range(10)]
print(squares)

# EX 3: LC in-lieu of a nested loop
pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append(num1, num2)
print(pairs_1)


pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2
           in range(6, 8)]
print(pairs_2)

# Note: Trade off of LC vs for-loop: READABILITY

# EX 3: LC in-lieu of a nested loop
pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append(num1, num2)
print(pairs_1)

# Practice #1: LC that produces a list of the first charar...
# ....of each string in doctor
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
result = [doc[0] for doc in doctor]
print(result)
# result==> ['h', 'c', 'c', 't', 'w']


# Practice #2: Create a 5 x 5 matrix using...
# ... nested list comprehensions

# Note: the output expression of the outer LC is a LC....
# ...the iterable of the outer LC loops w/o producing values....

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)

'''
