import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

# print(numbers)
# print("Shape:", numbers.shape)
# print("Type:", numbers.dtype)

import numpy as np

x = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(x)

print("Number of dimensions:", x.ndim)
print("Shape:", x.shape)
print("Total elements:", x.size)
print("Length:", len(x))

print("Element at row 0, column 1:", x[0, 1])

print("Sum along axis 0:", x.sum(axis=0))
print("Sum along axis 1:", x.sum(axis=1))