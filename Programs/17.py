import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.arange(1, 7, 2)
print(type(arr1))
print()
print(arr1)
print()
print(arr2)
print()
print(arr3)
print()
print(arr2[1][1])
print()
sumVal = 0
for arr in arr2 :
    for j in arr :
        sumVal += j
print(sumVal)