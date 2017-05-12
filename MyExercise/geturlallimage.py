import urllib.request
from io import BytesIO
import gzip

url = "http://www.baidu.com"

data = urllib.request.urlopen(url).read() #这里获取的数据 部分网站比如百度使用的是gizp压缩以后的数据

buff = BytesIO(data) #这里将压缩的数据转换为字节流

f = gzip.GzipFile(fileobj=buff)#根据字节流生成gzipfile的解压缩文件

res = f.read().decode('utf-8')#读取解压缩文件 获得真实的文件内容

print(res)