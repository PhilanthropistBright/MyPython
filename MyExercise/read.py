with open("D:/Elow/python/code/test/MyExercise/Txt/txt2.txt","a+") as f:

    f.write("""这里随便写一点
    是为了测试一下是否正确
    如果不正确 多指教""")
f.close()

with open("D:/Elow/python/code/test/MyExercise/Txt/txt2.txt","r") as f:
    str1 = f.read()

f.close()




import pickle

tempdata = {'class':'班级','age':33,'name':'林亮'}

with open("D:/Elow/python/code/test/MyExercise/Txt/txt3.ll","wb") as output:
    pickle.dump(tempdata,output)
output.close()

with open("D:/Elow/python/code/test/MyExercise/Txt/txt3.ll","rb") as f:
    detail = pickle.load(f)
    print(detail)

f.close()


