matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print(matrix[(0, 3)])

print(matrix.get((0, 3), 0))  # The first argument is the key; the second argument is the value get should return if the key is not in the dictionary:
print(matrix.get((1, 3), 0))