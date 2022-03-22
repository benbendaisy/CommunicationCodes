class MyQueue:

    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        if not self.stack1:
            self.stack1.append(x)
        else:
            stack2 = []
            while self.stack1:
                stack2.append(self.stack1.pop())
            self.stack1.append(x)
            while stack2:
                self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if self.stack1:
            return self.stack1.pop()
        return -1

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[0]
        return -1

    def empty(self) -> bool:
        return True if not self.stack1 else False

class MyQueue1:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        if self.stack1:
            return self.stack1.pop()
        return -1

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[-1]
        elif self.stack2:
            return self.stack2[0]
        return -1

    def empty(self) -> bool:
        return True if not self.stack1 and not self.stack2 else False

if __name__ == "__main__":
# Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(8)
    print(obj.pop())
    obj.push(3)
    print(obj.peek())
    print(obj.pop())
    obj.push(5)
    print(obj.pop())