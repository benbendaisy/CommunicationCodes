class MyHashMap:

    def __init__(self):
        self.length = 10000
        self.arr = [[] for _ in range(self.length)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.length
        self.remove(key)
        self.arr[idx].append((key, value))


    def get(self, key: int) -> int:
        idx = key % self.length
        length = len(self.arr[idx])
        if length > 0:
            for k, v in self.arr[idx]:
                if k == key:
                    return v
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.length
        length = len(self.arr[idx])
        element = None
        if length > 0:
            for k, v in self.arr[idx]:
                if k == key:
                    element = (k, v)
                    break
            if element:
                self.arr[idx].remove(element)