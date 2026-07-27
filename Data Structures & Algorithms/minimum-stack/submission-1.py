class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, value: int) -> None:
        minValue = self.getMin()
        if minValue == None or minValue > value:
            minValue = value

        self.stack.append([value, minValue])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None