import string
import math

s = 1

for i in range(1,11):
    print(repr(i).rjust(3,"0"),repr(pow(i,2)).rjust(4,"0"),repr(pow(i,3)).rjust(4,"0"))


#format

print('{name}您好，今年{age}岁'.format(name='林亮',age=34))

print("{0:.2f}".format(123.321))

print("test")