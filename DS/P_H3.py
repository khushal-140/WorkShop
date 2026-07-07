# class CicruleQueue:
#     def __init__(self,size):
#         self.size=size
#         self.queue=[None]*size
#         self.rear=-1
#         self.front=-1
        
#     def app(self,vechicalname):
#         if (self.rear+1)%self.size == self.front:
#             return "Packing is empty "
#         elif self.front==-1:
#             self.front=0
#             self.rear=0
#             self.queue[self.rear]=vechicalname
#         else:
#             self.rear=(self.rear+1)%self.size
#             self.queue[self.rear]=vechicalname
            
#     def dequeue(self):
#         if self.front==-1:
#             return "PAcking is full"
        
#         elif self.front==self.rear:
#             print("Remove Car",self.queue[self.front])
#             self.front=-1
#             self.rear=-1
#         else:
#             print("Remove Car",self.queue[self.front])
#             self.front=(self.front+1)%self.size


#     def display(self):
#         if self.front==-1:
#             return "Not vechical present at parking"
        
        
#         i=self.front
#         while True:
#             print(self.queue[i])
#             i==self.rear
#             break;  
                
#             i=i+1%self.size
                
        
        
# obj=CicruleQueue(65)
# obj.app("hi")

# obj.display()

class GPS:
    def __init__(self):
        self.fow=[None]*5
        self.back=[None]*5
        
    def visit(self,place):
        if self.fow is None:
            return "Not PLace you vist"
        else:
            self.fow.append(place)
            print("You are Entet in",place)
        
    def backk(self):
        f=self.fow.pop()
        print("You are moving back to previous location you vist=>",f)
        self.back.append(f)
    
    def forw(self):
        return "".join(self.backk)


obj=GPS()
obj.visit("Ahme")
obj.visit("MUbi")

print(obj.forw)

        