class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = []

    def push(self, val: int) -> None:
        # if len(self.stack)==0:
        #     self.Min=val
        #     return
        # self.Min=min(val,self.Min)
        # self.stack.append(val)
        self.stack.append(val)
#         if self.min contains elements
        if self.Min:
            val = min(val, self.Min[-1])
        # val = min(val, self.Min[-1] if self.Min else val)
        self.Min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.Min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
