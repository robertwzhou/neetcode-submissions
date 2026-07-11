class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if len(self.stack):
            self.stack.append((min(self.stack[-1][0], val), val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
