import collections


class MyStack1:
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1

class MyStack:

    def __init__(self):
        self.push_que = deque()
        self.pop_que = deque()
    def push(self, x: int) -> None:
        self.push_que.append(x)
        while self.pop_que:
            self.push_que.append(self.pop_que.popleft())
        self.push_que, self.pop_que = self.pop_que, self.push_que

    def pop(self) -> int:
        return self.pop_que.popleft()

    def top(self) -> int:
        return self.pop_que[0]

    def empty(self) -> bool:
        return not self.pop_que

if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())