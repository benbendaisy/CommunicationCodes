from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.idx = 0
        self.vector = [x for y in vec for x in y]

    def next(self) -> int:
        self.idx += 1
        return self.vector[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx < len(self.vector)