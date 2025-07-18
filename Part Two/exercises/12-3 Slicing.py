import numpy as np

colorful_array = np.array([[0, 1, 2, 3, 4, 5], 
                           [10, 11, 12, 13, 14, 15], 
                           [20, 21, 22, 23, 24, 25],
                           [30, 31, 32, 33, 34, 35],
                           [40, 41, 42, 43, 44, 45],
                           [50, 51, 52, 53, 54, 55],
                           ])

blue_array = colorful_array[:,1]  # Extracting rows 0 to 2 and columns 1 to 3
print(blue_array)

pink_array = colorful_array[1, 2:4]  # Extracting rows 2 to 3 and columns 1 to 3
print(pink_array)

orange_array = colorful_array[2:4, ::2]  # Extracting rows 2 to 3 and columns 3 to 5
print(orange_array)

orange_array = colorful_array[2:4, 4:6]
print(orange_array)
