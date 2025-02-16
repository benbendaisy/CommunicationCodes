from typing import List
from heapq import heappop, heappush, heapify

class KthLargest1:

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


class KthLargest2:

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


class KthLargest3:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) >= self.k and val > self.min_heap[0]:
            heapq.heappush(self.min_heap, val)
            heapq.heappop(self.min_heap)
        elif len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)