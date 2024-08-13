import numpy as np 
import sys
import time

# less memory
a = range(1000)
print(sys.getsizeof(2) * len(a))

array = np.arange(1000)
print(array.size * array.itemsize)

# faster and more convinient
SIZE = 1000000

list1 = range(SIZE)
list2 = range(SIZE)

array1 = np.arange(SIZE)
array2 = np.arange(SIZE)

start = time.time()
result = [(x+y) for x,y in zip(list1, list2)]
print(f'List took: {(time.time() - start)*1000}')

start = time.time()
result = array1 + array2
print(f'Numpy took: {(time.time()-start)*1000}')