import numpy as np
import time
import math

v1 = np.array([1, 2])
v2 = np.array([2, 2])


m = np.array([[1, 2], [3, 4], [5, 6]])
m = np.array([
             [1, 2],
             [3, 4],
             [5, 6]
             ])

print(m.shape)   # (3, 2) (fila, columna)
print(m.size)    # size=6 (3x2)
print(m.ndim)    # ndim=2 (array 2D)


#l1 = [x for x in range(5000)]


top = 5000000

print('Método SUM')

v1 = np.arange(top)
sum_v1 = np.sum(v1)

l1 = list(range(top))
sum_l1 = sum(l1)
        
time1 = time.time()
sum_v1 = np.sum(v1)
time2 = time.time()
numpy_time_ms = (time2-time1)*1000
print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

time1 = time.time()
sum_l1 = sum(l1)
time2 = time.time()
list_time_ms = (time2-time1)*1000
print('List time: {:.2f}ms'.format(list_time_ms))
print('SUM: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))

print('Método mean')

v1 = np.arange(top)
mean_v1 = np.mean(v1)

l1 = list(range(top))
mean_l1 = sum(l1) / len(l1)
        
time1 = time.time()
mean_v1 = np.mean(v1)
time2 = time.time()
numpy_time_ms = (time2-time1)*1000
print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

time1 = time.time()
mean_l1 = sum(l1) / len(l1)
time2 = time.time()
list_time_ms = (time2-time1)*1000
print('List time: {:.2f}ms'.format(list_time_ms))
print('MEAN: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))

print('Método sort')

v1 = np.arange(top)
sort_v1 = np.sort(v1)

l1 = list(range(top))
sort_l1 = l1.sort()
        
time1 = time.time()
sort_v1 = np.sort(v1)
time2 = time.time()
numpy_time_ms = (time2-time1)*1000
print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

time1 = time.time()
sort_l1 = l1.sort()
time2 = time.time()
list_time_ms = (time2-time1)*1000
print('List time: {:.2f}ms'.format(list_time_ms))
print('SORT: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))


print('Método Where')
lv1 = np.asanyarray(l1)
time1 = time.time()
np.where(lv1 % 2, v1, 0)
time2 = time.time()
numpy_time_ms = (time2-time1)*1000
print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

time1 = time.time()
[x if x % 2 else 0 for x in l1]
time2 = time.time()
list_time_ms = (time2-time1)*1000
print('List time: {:.2f}ms'.format(list_time_ms))
print('WHERE: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))


