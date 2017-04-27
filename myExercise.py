# import sys

# #斐波那契数列
# #解释：两个元素的总和确定了下一个数

# x = input("请输入最大的值:")

# a,b = 0,1
# print(a,end=',')
# print(b,end=',')

# while b < int(x):
#     a,b = b,a+b
#     print(b,end=',')



# def TestFunction(showmsg):
#     print(showmsg)

# TestFunction("aaa")



# #lambde使用

# sum = lambda a , b :a+b

# print(sum(1,2))


# #变量作用域

# num = 1

# def ChangeNumber():
#     global num
#     num = num +1
#     print(num)

# ChangeNumber()
# print(num)


#列表操作
list1 = [1,2,3,4]
list2 = [5,6,7]
# list1.append(list2)
list1.extend(list2)
list1.insert(1,10)
list1.remove(20)
print(list1)