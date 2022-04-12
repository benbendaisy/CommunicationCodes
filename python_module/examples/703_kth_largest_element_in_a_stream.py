from typing import List
from heapq import heappop, heappush, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        heapify(self.heap)
        for it in nums:
            self.add(it)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]


class KthLargest1:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        cur = 0
        while cur < len(self.nums) and self.nums[cur] > val:
            cur += 1
        self.nums.insert(cur, val)
        return self.nums[self.k - 1] if len(self.nums) >= self.k else -1


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)