class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user1=User("1","Ram")
user2=User("2","Mohith")
user3=User("3","kov")
user4=User("4","vasu")
user5=User("5","Anj")

user_list=[user1,user2,user3,user4,user5]

def follows(userx,usery):
    userx.follow(usery)
    print(f"{userx.name} Started following {usery.name}")
    print(f"Followers of {userx.name} are {userx.followers} and following is {userx.following}")
    print(f"Followers of {usery.name} are {usery.followers} and following is {usery.following}")
    print("\n")

for i in user_list:
    for j in user_list:
        if i != j:
            follows(i,j)
