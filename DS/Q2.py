class CircularQueue:
    def __init__(self, size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        
    def enqueue(self,Vechiclename):
        if(self.rear+1)%self.size==self.front:
            print("Queue is Full")
        
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=Vechiclename
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=Vechiclename
            
    def dequeue(self):
        if self.front==-1:
            print("Queue is Empty")
        
        elif self.front==self.rear:
            print("Removed Vehicle:",self.queue[self.front])
            self.front=-1
            self.rear=-1
        else:
            print("Removed Vehicle:",self.queue[self.front])
            self.front=(self.front+1)%self.size
        
    def display(self):
        if self.front==-1:
            print("Queue is Empty")
        i=self.front
        while True:
            print(self.queue[i],end=" ")
            if i==self.rear:
                break
            i=(i+1)%self.size
        print()

toll=CircularQueue(5)
toll.enqueue("Car1")
toll.enqueue("Car2")
toll.enqueue("Car3")
toll.dequeue()
toll.display()