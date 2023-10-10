class MyHashMap1:

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

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next
class MyHashMap:

    def __init__(self):
        self.length = 1000
        self.dict_cache = [ListNode() for i in range(self.length)]

    def hash(self, key):
        return key % self.length

    def put(self, key: int, value: int) -> None:
        cur = self.dict_cache[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.dict_cache[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.dict_cache[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next