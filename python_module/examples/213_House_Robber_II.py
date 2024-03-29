from typing import List


class Solution:
    """
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

        Example 1:

        Input: nums = [2,3,2]
        Output: 3
        Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
        Example 2:

        Input: nums = [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.
        Example 3:

        Input: nums = [1,2,3]
        Output: 3

        Constraints:

        1 <= nums.length <= 100
        0 <= nums[i] <= 1000
    """
    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1

    def rob(self, nums: List[int]) -> int:
        def robHelper(start, end):
            dp = [0] * (end - start)
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])
            for i in range(start + 2, end):
                dp[i - start] = max(dp[i - start - 1], dp[i - start - 2] + nums[i])
            return dp[-1]

        if not nums or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        return max(robHelper(0, len(nums) - 1), robHelper(1, len(nums)))
