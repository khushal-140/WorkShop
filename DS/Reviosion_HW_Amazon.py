class Amazon:
    def __init__(self):
        self.belt=[None]*8
        
    def add(self,product_name):
        if None in self.belt:   
            index=self.belt.index(None)
            self.belt[index]=product_name
        else:
            print("belt is full")
            
    def update(self,index,product_name):
        if 0<=index <8:
            self.belt[index]=product_name
        else:
            print("Invaild slot")
        
    def find(self,product_name):
        if product_name in self.belt:
            print("present",self.belt.index(product_name))
        else:
            print("Product is not present ")
        
    def full(self):
        if None in self.belt:
            print("not full")
        else:
            print(" Full") 
    
    
    
    def display(self):
        print( self.belt)
            


obj=Amazon()
obj.add("a")
obj.add("a")
obj.add("a")
obj.add("a")
obj.add("a")
obj.add("a")
obj.add("a")
obj.add("a")
obj.add("a")



obj.update(2,"xyz")

obj.full()
obj.display()