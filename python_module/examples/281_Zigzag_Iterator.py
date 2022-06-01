from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.arr = []
        for vl1, vl2 in zip(v1, v2):
            self.arr.append(vl1)
            self.arr.append(vl2)
        if len(v1) > len(v2):
            self.arr.extend(v1[len(v2):len(v1)])
        elif len(v1) < len(v2):
            self.arr.extend(v2[len(v1):len(v2)])
        self.idx = 0

    def next(self) -> int:
        res = self.arr[self.idx]
        self.idx += 1
        return res

    def hasNext(self) -> bool:
        return self.idx < len(self.arr)

if __name__ == "__main__":
    v1 = [1]
    v2 = []
    i, v = ZigzagIterator(v1, v2), []
    while i.hasNext():
        v.append(i.next())
    print(v)