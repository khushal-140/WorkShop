class CQ:
    def __init__(self):
        self.queue=[None]*5
        self.front=-1
        self.rear=-1
    
    def full(self):
        return (self.rear+1)%5==self.front
    
    def isempty(self):
        return self.front==-1
    
    def enqueue(self,data):
        if self.full():
            print("Queue is full")
            return
        if self.front==-1:
            self.front=0
            self.rear=0
        else:
            self.rear=(self.rear+1)%5
        self.queue[self.rear]=data
        
    def dequeue(self):
        if self.isempty():
            print("Not element for dequeue")
            return
        data=self.queue[self.front]
        self.queue[self.front]=None
        if self.front== self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%5
        return     data
obj=CQ()
obj.enqueue(10)
print(obj.dequeue())
            
            
            
            