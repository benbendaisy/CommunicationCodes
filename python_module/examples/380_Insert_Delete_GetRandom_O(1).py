import random


class RandomizedSet1:
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

class RandomizedSet2:

    def __init__(self):
        self.arr = []
        self.value_idx = {}
        self.idx = -1

    def insert(self, val: int) -> bool:
        if val in self.value_idx:
            return False
        self.idx += 1
        self.value_idx[val] = self.idx
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not self.arr or val not in self.value_idx:
            return False
        v, t = self.arr[self.idx], self.value_idx[val]
        self.arr[t], self.arr[self.idx] = self.arr[self.idx], self.arr[t]
        self.value_idx[v] = t
        del self.value_idx[val]
        self.arr.pop()
        self.idx -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
    

class RandomizedSet3:

    def __init__(self):
        self.set_dict = {}
        self.set_list = []

    def insert(self, val: int) -> bool:
        if val in self.set_dict:
            return False
        self.set_dict[val] = len(self.set_list)
        self.set_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set_dict:
            last, idx = self.set_list[-1], self.set_dict[val]
            self.set_list[idx], self.set_dict[last] = last, idx
            self.set_list.pop()
            del self.set_dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.set_list)

class RandomizedSet:

    def __init__(self):
        self.set_dict = {}
        self.set_list = []

    def insert(self, val: int) -> bool:
        if val in self.set_dict:
            return False
        self.set_dict[val] = len(self.set_list)
        self.set_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set_dict:
            return False
        
        last_element, idx = self.set_list[-1], self.set_dict[val]
        self.set_list[idx], self.set_list[-1] = self.set_list[-1], self.set_list[idx]
        self.set_dict[last_element] = idx
        del self.set_dict[val]
        self.set_list.pop() # delete the last element
        return True
    def getRandom(self) -> int:
        return choice(self.set_list)