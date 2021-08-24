from os import system
import numpy as np
system('cls')

# Construindo um [array 2D Numpy] com valores numéricos em formato STRING:
arr = np.array(np.arange(1, 10).reshape(3, 3), dtype="U1")
print("Array 2D Numpy com strings:")
print(arr)
print()

# Atribuindo valores STRING em elementos do [array 2D Numpy]:
arr[0][1] = "X"
arr[1][1] = "X"
arr[2][1] = "X"
print("Array 2D Numpy modificado:")
print(arr)
print()

# Iterando colunas com método Numpy:
print("Segunda coluna do array 2d:")
temp = arr[0:3, 1]
print("temp =", temp)
print()


# Comparando resultado de colunas com dados:
if arr[:, 1].all(dtype="U1") == ['X' 'X' 'X']:
    print("Você perdeu.")