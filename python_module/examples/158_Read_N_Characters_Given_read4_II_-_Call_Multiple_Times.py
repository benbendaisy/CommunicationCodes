import collections
from typing import List


class Solution:
    def __init__(self):
        self.q = []
        self.queue = collections.deque()

    def read1(self, buf: List[str], n: int) -> int:
        copied = 0
        buf4 = [""] * 4
        while copied < n:
            if self.q:
                buf[copied] = self.q.pop(0)
                copied += 1
            else:
                readCnt = read4(buf4)
                if readCnt == 0:
                    break
                self.q += buf4[:readCnt]

        return copied

    def read(self, buf: List[str], n: int) -> int:
        copied = 0
        buf4 = [""] * 4
        while copied < n:
            if self.queue:
                buf[copied] = self.queue.popleft()
                copied += 1
            else:
                readCnt = read4(buf4)
                if readCnt == 0:
                    break
                self.queue += buf4[:readCnt]
        return copied