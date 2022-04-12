from collections import defaultdict
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            arr[nums[i]] += 1
        dup = missing = 0
        for i in range(1, len(nums) + 1):
            if arr[i] == 0:
                missing = i
            elif arr[i] == 2:
                dup = i
        return [dup, missing]

    def findErrorNums1(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        countMap = defaultdict(int)
        dup = missing = 0
        for i in range(len(nums)):
            countMap[nums[i]] += 1
            if countMap[nums[i]] == 2:
                dup = nums[i]

        for i in range(1, len(nums[i]) + 1):
            if i not in countMap:
                missing = i

        return [dup, missing]