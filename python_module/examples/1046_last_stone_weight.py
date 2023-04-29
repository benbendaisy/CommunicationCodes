from typing import List


class Solution:
    def lastStoneWeight1(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones.sort(reverse=True)
        l = stones[2:]
        l.append(abs(stones[0] - stones[1]))
        return self.lastStoneWeight(l)

    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for stone in stones:
            heapq.heappush(arr, -stone)
        # heapq.heapify(stones)
        while len(arr) > 1:
            diff = abs(heapq.heappop(arr) - heapq.heappop(arr))
            heapq.heappush(arr, -diff)
        return -arr[0]
