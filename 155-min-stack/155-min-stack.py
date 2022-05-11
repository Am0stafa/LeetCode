class MinStack:

    def __init__(self):
        self.stack = []
        self.currentMin = []
            
    def push(self, val: int) -> None:
        self.stack.append(val)
        
         
        if not self.currentMin or val < self.currentMin[-1]:
            self.currentMin.append(val) 
        else:
            self.currentMin.append(self.currentMin[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.currentMin.pop()

    def top(self) -> int:
        return self.stack[-1]
           
    def getMin(self) -> int:
        return self.currentMin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()