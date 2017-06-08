class MyClass:
    i=12345
    def f(self):
        return "hello world"

x= MyClass()

print(x.i)
print(x.f())


class MyClass1:
    sum = 0
    def __init__(self,sum1,sum2):
        self.sum = sum1+sum2
        self.su1=sum1
        self.su2=sum2

y = MyClass1(10,20)

print(y.sum,y.su1,y.su2)
