# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if self.stack:
            min = self.min[len(self.min)-1]
            if val < min:
                self.min.append(val)
            else:
                self.min.append(min)
        else:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min[len(self.min)-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# T = O(1)
# S = O(N)