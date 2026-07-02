class GPS:
    def __init__(self):
        self.backStack=[]
        self.forwardStack=[]
        self.currentLocation=None
        
    def visit(self,place):
        if self.currentLocation is not None:
            self.backStack.append(self.currentLocation)
        self.currentLocation=place
        self.forwardStack.clear()
        
    def back(self):
        if not self.backStack:
            print("No previous location.")
            return
        self.forwardStack.append(self.currentLocation)
        self.currentLocation=self.backStack.pop()
        print("Current Location:",self.currentLocation)
        
    def forward(self):
        if not self.forwardStack:
            print("No forward location.")
            return
        self.backStack.append(self.currentLocation)
        self.currentLocation=self.forwardStack.pop()
        print("Current Location:",self.currentLocation)
    
    def show(self):
        print("Current Location:",self.currentLocation)

gps=GPS()
gps.visit("Place1")
gps.visit("Place2")
gps.visit("Place3")
gps.back()
gps.show()