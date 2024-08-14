import numpy as np

a = np.array([4, 5, 6])
b = np.array([[1,2], [5, 6], [9, 8]])
c = np.array([1, 2, 3], dtype=float)

print(f'{a.ndim}, {b.ndim}')
print(f'a = {a.dtype}, {a.itemsize} \nb = {b.dtype}, {b.itemsize} \nc = {c.dtype}, {c.itemsize}')

print(np.arange(0, 11, 2))

d = np.array([[1,2], [3, 4], [5, 6]])
print(f'{d} \nshape = {d.shape}')
print(f'reshape (2, 3) = \n{d.reshape(2,3)}')
print(f'reshape (1, 6) = \n{d.reshape(6,1)}')
print(f'sum: {d.sum(axis=0)}') # axis = 0 represents columns, axis = 1, rows