import numpy as np

# Question 1: Create a 2x3 matrix and multiply it by 2
array_A = ([[6, -9, 1], [4, 24, 8]])
print(2 * array_A)

# Question 2: Create a 2x3 matrix and a 2x2 matrix, then compute their dot product
array_B = ([[1, 0], [0, 1]])
result = np.dot(array_B, array_A)
print(result)

# Question 3: Create a 2x2 matrix and a 2x2 matrix, then compute their dot product
array_C = ([[4, 3], [3, 2]])
array_D = ([[-2, 3], [-3, 4]])

result = np.dot(array_C, array_D)
print(result)
