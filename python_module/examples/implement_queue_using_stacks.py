class MyQueue:
    stack1 = []
    stack2 = []
    def push(self, x: int) -> None:
        stack2.append(x)
        if stack1.empty():
            while !stack2.empty:
                stack1.append(stack2.pop())

    def pop(self) -> int:
        if stack1.empty():
            while not stack2.empty:
                stack1.append(stack2.pop())
        if not stack1.empty():
            stack1.pop()

    def peek(self) -> int:
        if stack1.empty():
            return -1
        return stack1[0]

    def empty(self) -> bool:
        return true if not stack1 else false


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()