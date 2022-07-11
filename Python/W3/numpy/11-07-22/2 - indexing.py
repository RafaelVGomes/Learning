import numpy as np

# arr = np.array([1, 2, 3, 4])
# print(arr[0])
# print(arr[1])
# print(arr[2] + arr[3])

# 2-D Arrays
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(f'2nd element on 1st row: {arr[0, 1]}')
# print(f'5th element on 2nd row: {arr[1][4]}')

# 3-D Arrays
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])

# Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(f'Last element from 2nd dim: {arr[1, -1]}')