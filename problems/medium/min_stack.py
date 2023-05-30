class MinStack:
    s = []
    def __init__(self):
        MinStack.s = []    

    def push(self, val: int) -> None:
        MinStack.s.append(val)

    def pop(self) -> None:
        return MinStack.s.pop() if len(MinStack.s) else None

    def top(self) -> int:
        return MinStack.s[-1] if len(MinStack.s) else None

    def getMin(self) -> int:
        return min(MinStack.s)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()