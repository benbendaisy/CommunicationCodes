from typing import List


class Solution:
    """
        An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

        For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
        Given an integer array nums, return the number of arithmetic subarrays of nums.

        A subarray is a contiguous subsequence of the array.

        Example 1:

        Input: nums = [1,2,3,4]
        Output: 3
        Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
        Example 2:

        Input: nums = [1]
        Output: 0
    """
    def numberOfArithmeticSlices1(self, nums: List[int]) -> int:
        cnt = 0
        m = len(nums)
        for i in range(m - 2):
            dx = nums[i + 1] - nums[i]
            for j in range(i + 2, m):
                if nums[j] - nums[j - 1] == dx:
                    cnt += 1
                else:
                    break
        return cnt

    def numberOfArithmeticSlices2(self, nums: List[int]) -> int:
        self.x = 0
        def slices(idx):
            if idx < 2:
                return 0
            ap = 0
            if nums[idx] - nums[idx - 1] == nums[idx - 1] - nums[idx - 2]:
                ap = 1 + slices(idx - 1)
            else:
                slices(idx - 1)
            self.x += ap
            return ap
        slices(len(nums) - 1)
        return self.x

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [0] * m
        sums = 0
        for i in range(2, m):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = 1 + dp[i - 1]
                sums += dp[i]
        return sums