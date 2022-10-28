from collections import defaultdict
from typing import List


class Solution:
    """
        Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

        Example 1:

        Input: nums = [1,2,3,1], k = 3
        Output: true
        Example 2:

        Input: nums = [1,0,1,1], k = 1
        Output: true
        Example 3:

        Input: nums = [1,2,3,1,2,3], k = 2
        Output: false
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2:
            return False

        numDict = defaultdict(list)
        for idx, num in enumerate(nums):
            if num in numDict:
                for ix in numDict[num]:
                    if idx - ix <= k:
                        return True
            numDict[num].append(idx)
        return False
