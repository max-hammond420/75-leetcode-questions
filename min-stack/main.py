import sys


class MinStack:

    def __init__(self):
        self.ls = []

    def push(self, val: int) -> None:
        self.ls.append(val)

    def pop(self) -> None:
        self.ls = self.ls[:-1]

    def top(self) -> int:
        return self.ls[-1]

    def getMin(self) -> int:
        current_min = sys.maxsize
        for i in self.ls:
            current_min = min(i, current_min)
        return current_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
