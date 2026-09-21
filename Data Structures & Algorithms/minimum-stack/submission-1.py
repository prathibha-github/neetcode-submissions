class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
            return
        else:
            if self.mins[-1] < val:
                self.mins.append(self.mins[-1])
            else:
                self.mins.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.mins.pop()
            

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return float('inf')

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
        return float('inf')
        
