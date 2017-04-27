class Animal:
    name=""
    age=0
    __attr=""
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def Show(self):
        print("name is {},age is {}".format(self.name,self.age))
    

class Tiger(Animal):
    
    def __init__(self,name,age,color):
        Animal.__init__(self,name,age)
        self.color = color
    def Show(self):
        print("name is {},age is {},color is {}".format(self.name,self.age,self.color))

a = Tiger("mingzi","nianling","Red")
a.Show()

