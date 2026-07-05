class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def addlinked(self,data):
        newnode=node(data)
        
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode


        
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,"=>",end="")
            temp=temp.next
        print("Null")
    
    def count(self):
        countt=0
        temp=self.head
        while temp is not None:
            countt += 1
            temp=temp.next
        print(countt)
        
    def serch(self,key):
        temp=self.head
        found=0
        while temp is not None:
            if temp.data == key:
                found=1
                break
            temp=temp.next
                
        if found==1:
            print(key,"Found")
        else:
            print(key,"data not found")

li=LinkedList()
li.addlinked(10)
li.addlinked(20)
li.addlinked(30)
li.display()
li.count()
li.serch(10)
        
    
        
        