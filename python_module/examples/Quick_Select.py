import random
from typing import List


class QuickSelect:
    def partition(self, arr:List[int], l: int, r: int):
        pivot = random.randint(l, r)
        arr[pivot], arr[r] = arr[r], arr[pivot]
        pivot, ptr = arr[pivot], l
        for i in range(l, r):
            if arr[i] <= pivot:
                arr[i], arr[ptr] = arr[ptr], arr[i]
                ptr += 1
        arr[ptr], arr[r] = arr[r], arr[ptr]
        return ptr

    def findTopK(self, arr: List[int], k: int):
        l, r = 0, len(arr) - 1
        while l < r:
            p = self.partition(arr, l, r)
            if p == k:
                return arr[p]
            elif p < k:
                l = p + 1
            else:
                r = p - 1
        return arr[l]