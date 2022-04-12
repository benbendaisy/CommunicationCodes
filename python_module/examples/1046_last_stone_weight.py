from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones.sort(reverse=True)
        l = stones[2:]
        l.append(abs(stones[0] - stones[1]))
        return self.lastStoneWeight(l)
