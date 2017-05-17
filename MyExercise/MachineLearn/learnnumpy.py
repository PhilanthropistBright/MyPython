import numpy as np

#np.random.rand(3,10) 随机产生 3组  每组10个的矩阵

x_data = np.float32(np.random.rand(2,100))#随机输入

print(x_data)


y_data = np.dot([0.100,0.200],x_data)#随机输入

print(y_data)