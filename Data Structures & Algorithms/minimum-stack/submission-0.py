class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        minimum = val
        if self.stack:
            minimum = min(val, self.getMin())
        self.stack.append((val, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
