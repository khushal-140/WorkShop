class Conveyor:
    def __init__(self):
        self.bel=[None]*8
    
    def updateslot(self,index,product):
        self.bel[index]=product
    
    def checkslot(self,index):
        return self.bel[index]
    
    def findproduct(self,product):
        if product in self.bel:
            print(f"{product} is present in the conveyor belt.")
    
    def full(self):
        if None not in self.bel:
            print("The conveyor belt is full.")
        else:
            print("The conveyor belt is not full.")
    
obj=Conveyor()
print(obj.bel)
obj.updateslot(0,"Product1")
print(obj.bel)
print(obj.checkslot(0))
print(obj.findproduct("Product1"))
obj.full()