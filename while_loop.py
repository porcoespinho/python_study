
# example of WHILE loop with IF statement
offset = -6
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
        print(offset)
    else:
        offset = offset + 1
        print(offset)
