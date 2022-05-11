from collections import defaultdict
from typing import List


class Solution:
    def maxOperations1(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        l, r = 0, len(nums) - 1
        cnt = 0
        while l < r:
            t = nums[l] + nums[r]
            if t == k:
                cnt += 1
                l, r = l + 1, r - 1
            elif t < k:
                l += 1
            else:
                r -= 1
        return cnt

    def maxOperations(self, nums: List[int], k: int) -> int:
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1
        cnt = 0
        for num in nums:
            component = k - num
            if num == component and numMap[num] < 2:
                continue

            if numMap[num] > 0 and numMap[component] > 0:
                numMap[component] -= 1
                numMap[num] -= 1
                cnt += 1
        return cnt
