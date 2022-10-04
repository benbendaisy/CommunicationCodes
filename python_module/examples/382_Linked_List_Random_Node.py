# Definition for singly-linked list.
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        k = 1
        if not self.arr:
            return -1
        res = [0] * k
        for i in range(k):
            res[i] = self.arr[i]

        while i < len(self.arr):
            r = random.randrange(i + 1)
            if r < k:
                res[r] = self.arr[i]
            i += 1
        return res[0]