class addition:
    first=0
    second=0
    total=0

    def __init__(self,f,s):
        self.first=f
        self.second=s

    def fun(self):
        print("First number:",self.first)
        print("Second number:",self.second)
        print("Total is",self.total)

    def calc(self):
        self.total=self.first+self.second

obj1=addition(100,200)
obj1.calc()
obj1.fun()
