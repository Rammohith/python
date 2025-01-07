class dog:
    breed1="lab"
    breed2="pug"

    def fun(self):
        print("Im a",self.breed1)
        print("Im a",self.breed2)

obj=dog()
print("this dog is a",obj.breed1)

obj.fun()