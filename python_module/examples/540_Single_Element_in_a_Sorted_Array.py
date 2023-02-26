from typing import List


class Solution:
    """
        You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

        Return the single element that appears only once.

        Your solution must run in O(log n) time and O(1) space.

        Example 1:

        Input: nums = [1,1,2,3,3,4,4,8,8]
        Output: 2
        Example 2:

        Input: nums = [3,3,7,7,10,11,11]
        Output: 10
    """
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        if not nums:
            return -1

        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res

    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) // 2
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            idx = mid * 2
            if idx + 1 >= len(nums) or nums[idx] != nums[idx + 1]:
                ans = nums[idx]
                r = mid - 1
            else:
                l = mid + 1
        return ans
