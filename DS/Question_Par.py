# li=["amit","kiwi","will","rahel","smit"]
# name=input("Enter name to check the arrival:")
# for i in range(len(li)):
#     if li[i] == name.lower():
#         print(name,"is arrival entry")
#         break
# else:
# #     print(name,"not arrival")

# class Hospital:
#     def __init__(self):
#         self.normal=[]
#         self.emergency=[]
    
#     def addPatient(self,name,pri):
#         if pri == "emergency":
#             self.emergency.append(name)
#         else:
#             self.normal.append(name)
   
        
#     def treatment(self,pri):
#         if pri == "emergency":
#             return "".join(self.emergency)
#         else:
#             return "".join(self.normal)
    
#     def dispaly(self):
#         return "".join(self.emergency)
    
# obj=Hospital()
# obj.addPatient("Amit","noral")
# obj.addPatient("Rahel","emergency")
# print(obj.dispaly())




# class Whatapp:
    
#     def __init__(self):
#         self.waht=[None]
        
#     def type(self,char):
#         self.waht.append(char)
    
#     def undo(self):
#         last=self.waht.pop()
#         return last
    
#     def show(self):
#         return self.waht

# obj=Whatapp()
# obj.type("a")
# obj.type("b")
# obj.type("c")
# print(obj.undo())
# obj.undo()
# print(obj.show())


# class Pump:
#     def __init__(self):
#         self.vechical=[None]*5
#         self.front=-1
#         self.rear=-1
        
#     def enqueue(self,Veciclaname):
#         if (self.rear+1)%5 ==self.front:
#             return "full"
    
#         elif self.front==-1:
#             self.front=0
#             self.rear=0
#             self.vechical[self.rear]=Veciclaname
#         else:
#             self.rear=(self.rear+1)%5
#             self.vechical[self.rear]=Veciclaname
        
#     def dequeu(self):
#         if self.front==-1:
#             return "not car the "
        
#         elif self.front==self.rear:
#             print(self.vechical[self.front])
#             self.front=-1
#             self.rear=-1
#             #self.front=(self.front+1)%5
        
#         else:
#             print(self.vechical[self.front])
#             self.front=(self.front+1)%5
   
            
# obj=Pump()
# obj.enqueue("Car 1")
# obj.enqueue("Car 2")
# obj.dequeu()
# obj.dequeu()
# obj.dequeu()
# print(obj.dequeu())
# obj.enqueue("CAr ")
# obj.dequeu()
# obj.enqueue("Car 2")
# obj.enqueue("Car 2")
# obj.enqueue("Car 2")
# obj.enqueue("Car 2")

# obj.enqueue("Car 2")
# print(obj.enqueue("Car 2"))




# li=[99,10,100,200,400,80]
# for i in range(len(li)):
#     for j in range(len(li)-i-1):
#         if li[j]>li[j+1]:
#             temp=li[j]
#             li[j]=li[j+1]
#             li[j+1]=temp
# print(li[::-1])






# li=["ABC","BCD","CDE","EFG"]
# low=0
# high=len(li)
# key="ABC"
# while low<high:
#     mid=low+high//2
    
#     if li[mid]==key:
#         print(key,"is found at index",mid)
#         break
#     elif li[mid]<key:
#         low=mid+1
#     else:
#         high=mid-1
# else:
#     print(key,"not present in libar")
        

# class Grogry:
#     def __init__(self):
#         self.li=["Rice","Oil","Suger","Mike","Tea"]
#     def add(self,productname):
#         #productname=input("Enter Product name:")
#         self.li.append(productname)
#     def Serach(self,name):
#         for i in self.li:
#             if i == name:
#                 return f"{name} is present in store"
#         else:
#             return f"{name}  not present in store"
        
#     def update(self,index,pro):
#         self.li[index-1]=pro
        
#     def dispaly(self):
#         return self.li
        
# obj=Grogry()
# print(obj.dispaly())
# obj.add("coffer")
# print(obj.Serach("Tea"))

# print(obj.dispaly())
# obj.add("MAgic")
# obj.update(7,"Teaaa")
# print(obj.dispaly())



class Pri:
    def __init__(self):
        self.vip=[]
        self.gen=[]
    
    def book(self,name,pr):
        if pr =="vip":
            self.vip.append(name)
        else:
            self.gen.append(name)
            
    def cancel(self,pri):
        if pri == "vip":
            c=self.vip.pop(0)
            print("Ticket Cacel",c)
        else:
            c=self.gen.pop(0)
            print("Ticket Cacel",c)
    
    def dispaly(self):
        print("VIP")
        for i in self.vip:
            print(i)
        print("GEnreal")
        for i in self.gen:
            print(i)

obj=Pri()
obj.book("Rahel","vip")
obj.book("Amit","Genral")
obj.book("Ahm","vip")
obj.book("smit","genrel")
obj.cancel("vip")
obj.dispaly()