class MinStack:

    def __init__(self):
        self.stack = []
        self.extra = []

    def push(self, val: int) -> None:
        if not self.extra:
            self.extra.append(val)
            self.stack.append(val)
            return

        self.extra.append(min(val, self.extra[-1]))
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop()
        self.extra.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extra[-1]
