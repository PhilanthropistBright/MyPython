f = open("D:/Elow/python/code/test/MyExercise/Txt/txt2.txt","a+")

f.write("""这里随便写一点
是为了测试一下是否正确
如果不正确 多指教""")

f.close()

f = open("D:/Elow/python/code/test/MyExercise/Txt/txt2.txt","r")

str1 = f.read()

f.close()

print(str1)

