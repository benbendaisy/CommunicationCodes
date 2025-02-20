import math
from typing import List


class Solution:
    """
        You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

        Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

        0 <= j <= nums[i] and
        i + j < n
        Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

        Example 1:

        Input: nums = [2,3,1,1,4]
        Output: 2
        Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
        Example 2:

        Input: nums = [2,3,0,1,4]
        Output: 2
    """
    def jump1(self, nums: List[int]) -> int:
        ans, end, n = 0, 0, len(nums)
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, nums[i] + i)
            if farthest >= n - 1:
                ans += 1
                break
            if i == end:
                ans += 1
                end = farthest
        return ans

    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [math.inf for _ in range(n)]
        memo[0] = 0
        for i in range(n):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= n:
                    break
                elif memo[j] > memo[i] + 1:
                    memo[j] = memo[i] + 1
        return memo[n - 1]
    
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0
        for i, _ in enumerate(nums):
            for j in range(0, i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]