# li=["a"]*10
# no=int(input("Enter Roll number to mark present"))
# li.insert(no,"P")
# for i in range(len(li)):
#     print(i,li[i])

class Stack:
    def __init__(self):
        self.edit=[]
    
    def type(self,char):
        self.edit.append(char)
        
    def undo(self):
        return self.edit.pop()
    
    def getText(self):
        return self.edit[-1]
    
    def dispaly(self):
        return "".join(self.edit)

obj=Stack()
obj.type("a")
obj.type("b")
obj.type("c")
print("pop:",obj.undo())
print(obj.getText())
print(obj.dispaly())