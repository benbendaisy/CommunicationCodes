from functools import lru_cache
from typing import List


class Solution:
    """
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

        Example 1:

        Input: nums = [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.
        Example 2:

        Input: nums = [2,7,9,3,1]
        Output: 12
        Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
        Total amount you can rob = 2 + 9 + 1 = 12.

        Constraints:

        1 <= nums.length <= 100
        0 <= nums[i] <= 400
    """
    def rob0(self, nums: List[int]) -> int:
        if not nums:
            return 0

        @lru_cache(None)
        def robHelper(idx: int):
            if idx == len(nums):
                return 0

            robbed = nums[idx] + robHelper(idx + 2)
            notRobbed = robHelper(idx + 1)
            return max(robbed, notRobbed)

        return robHelper(0)

    def rob1(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]

    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(1, n):
            for j in range(0, i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp)
    
    def rob3(self, nums: List[int]) -> int:
        m = len(nums)
        @cache
        def helper(idx: int):
            if idx >= m:
                return 0
            max_profit = 0
            for i in range(idx, m):
                max_profit = max(max_profit,nums[i] + helper(i + 2))
            return max_profit
        return helper(0)
    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        @cache
        def helper(idx: int) -> int:
            if idx >= n:
                return 0
            # skip
            opt1 = helper(idx + 1)
            opt2 = nums[idx] + helper(idx + 2)
            return max(opt1, opt2)
        return helper(0)


