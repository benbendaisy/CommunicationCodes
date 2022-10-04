import random


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.cache = {}

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False
        self.arr.append(val)
        self.cache[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False

        lastElement, idx = self.arr[-1], self.cache[val]
        self.arr[idx], self.cache[lastElement] = lastElement, idx
        del self.cache[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.arr) - 1)
        return self.arr[idx]
