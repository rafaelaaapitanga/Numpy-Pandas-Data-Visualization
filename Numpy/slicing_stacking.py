import numpy as np

a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
print(a)

print(a[1, 2])
print(a[0:2, 2]) # rows from 0 to 1 (2 doesnt count) and the second column

for cell in a.flat:
    print(cell)