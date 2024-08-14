import numpy as np

a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)

sticking_v = np.vstack((a, b)) # add top-down
sticking_h = np.hstack((a, b)) # add side by side
print(sticking_v)
print(sticking_h)

c = np.arange(12).reshape(3, 4)
print(c)

d = c > 4
print(d)

print(c[d]) # only the numbers > 4

c[d] = -1 # replacing to -1 the numbers > 4
print(c)