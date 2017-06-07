from numpy import *

a = arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))

b = array([(1.5,2,3),(4,5,6),(4,5,6)])
print(b.ndim)
#arange参数 起始数字  截至数字  数字的间隔
c = arange(0,30,5)
print(c)
