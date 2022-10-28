import math
from typing import List


class Solution:
    """
        Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

        Return the sum of the three integers.

        You may assume that each input would have exactly one solution.

        Example 1:

        Input: nums = [-1,2,1,-4], target = 1
        Output: 2
        Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
        Example 2:

        Input: nums = [0,0,0], target = 1
        Output: 0
        Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

        Constraints:

        3 <= nums.length <= 1000
        -1000 <= nums[i] <= 1000
        -104 <= target <= 104
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return -1
        diff = math.inf
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            lo, hi = i + 1, n - 1
            while lo < hi:
                sums = nums[i] + nums[lo] + nums[hi]
                if sums == target:
                    return sums
                if abs(target - sums) < abs(target - ans):
                    ans = sums
                if sums < target:
                    lo += 1
                else:
                    hi -= 1
        return ans
