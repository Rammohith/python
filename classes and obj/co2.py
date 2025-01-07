class dog:
    animal='dog'

    def __init__(self,breed,color):
        self.breed=breed
        self.color=color

obj1=dog("pug","black")
obj2=dog("lab","white")

print("rodgerr detailsss......")
print("Rodger is a",obj1.animal)
print("Rodger is",obj1.breed)
print("Rodger is",obj1.color)
print("Buzz detailssssss......")
print("buzz is a",obj2.animal)
print("buzz is a",obj2.breed)
print("buzz is ",obj2.color)