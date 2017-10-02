import numpy as np
arr1 = np.zeros((3, 3))
arr2 = np.zeros((3, 3))
arr2[1][1] = 8
res = np.array_equal(arr1, arr2)
print(res)
