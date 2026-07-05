class Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueu(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue.pop(0)

    def peak(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue)==0
    
    def display(self):
        return (self.queue)
    
obj=Queue()
obj.enqueu(10)
obj.enqueu(20)
obj.enqueu(30)
obj.dequeue()
print("Peek",obj.peak())
print(obj.display())