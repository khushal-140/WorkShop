class PrioritQueue:
    def __init__(self):
        self.nor=[]
        self.urg=[]
    
    def enqueue(self,name):
        if name=="Urgent":
            self.urg.append(name)
        else:
            self.nor.append(name)
    
    def dequeue(self,name):
        if name=="Urgent":
            return self.urg.pop(0)
        else:
            return self.nor.pop(0)
    
    def display_nor(self):
        return "".join(self.nor)
    
    def display_urg(self):
        return "".join(self.urg)

obj=PrioritQueue()
obj.enqueue("hi")
obj.enqueue("Urgent")
print(obj.display_nor())
print(obj.display_urg())