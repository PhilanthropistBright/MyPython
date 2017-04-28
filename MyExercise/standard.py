#操作系统
import os
# print(os.getcwd())#当前工作目录

# os.chdir("/server")#修改工作目录

# os.system("mkdir today") #执行系统命令mkdir

# print(dir())#所有引用

# print(help())#相关帮助


#日常文件和目录管理任务
import shutil

# shutil.copyfile("MyExercise/input.py","MyExercise/input22.py") #复制文件

# shutil.move("input.py","myexercise/input.py") #移动文件


#文件通配符
import glob
# print(glob.glob("myexercise/*.py")) #查找制定目录下的所有.py结尾的文件

#命令行参数
import sys
# print(sys.argv) #获得命令行参数 第一个为文件当前路径

#正则匹配
import re
# print(re.findall(r'\bf[a-z]*',"which foot or hand fell fastest"))

#数学
import math
# print(math.pow(2,3))

#随机数 
import random
# print(random.choice(["a","b","c"]))#随机选择

# print(random.sample(range(100),10)) #不重复抽样

# print(random.random()) #1以内的随即小数

# print(random.randrange(3)) #大于等于0 小于3的随机整数

#互联网
# from urllib.request import urlopen
# for line in urlopen("http://172.17.17.168/Default.aspx"):
#     line = line.decode("utf-8")
#     if "EST" in line or "EDT" in line:
#         print(line)


#日期和时间
# from datetime import date
# print(date.today())#当前日期

# # %b月份简写 %B月份全部  %A 星期几
# print(date.today().strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

#数据压缩
# import zlib,base64
# s= b"Base64 encoding is a kind of \"gentleman do not prevent a\" proof of encoding.Widely used in the MIME protocol, as email transfer encoding, the generated code reversible, one might be \"=\", after the generated code are ASCII characters.Advantages: fast, ASCII characters, do not understand to the naked eyeFaults: long code comparison, very easy to be cracked, applies only to encrypt the occasion of non-critical informationPython Base64 encoding and decoding"
# es = base64.b64encode(s)#转义base64
# print(len(es))
# t=zlib.compress(es)#数据压缩
# print(len(t))

# print(base64.b64decode(zlib.decompress(t)))#数据解压并还原base64

# zlib.crc32(a)#crc压缩


#性能度量
from timeit import Timer


# print(Timer('a,b = b,a', 'a=1; b=2').timeit(1000000))

# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit(1000000))#这里的1000是执行次数 默认不写default_number = 1000000


#测试模块
import doctest

# def average(values):
#     return sum(values) / len(values)

# print(doctest.testmod())

