class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []    

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        temp_stack = []
        while self.min_stack and self.min_stack[-1] < val:
            temp_stack.append(self.min_stack.pop())
        self.min_stack.append(val)
        while temp_stack:
            self.min_stack.append(temp_stack.pop())
    
    def pop(self) -> None:
        target = self.stack.pop()
        temp_stack = []
        while self.min_stack[-1] < target:
            temp_stack.append(self.min_stack.pop())
        self.min_stack.pop()
        while temp_stack:
            self.min_stack.append(temp_stack.pop())

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()