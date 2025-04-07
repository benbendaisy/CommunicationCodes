from functools import lru_cache
from typing import List


class Solution:
    """
        Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

        Example 1:

        Input: nums = [1,5,11,5]
        Output: true
        Explanation: The array can be partitioned as [1, 5, 5] and [11].
        Example 2:

        Input: nums = [1,2,3,5]
        Output: false
        Explanation: The array cannot be partitioned into equal sum subsets.
    """
    def canPartition1(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(idx, subset_sum):
            if subset_sum == 0:
                return True

            if idx == 0 or subset_sum < 0:
                return False

            return dfs(idx - 1, subset_sum - nums[idx]) or dfs(idx - 1, subset_sum)

        sums = sum(nums)
        if sums % 2 != 0:
            return False

        return dfs(len(nums) - 1, sums // 2)

    def canPartition2(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            cur = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < cur:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - cur]
        return dp[n][subset_sum]
    
    def canPartition3(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        n = len(nums)
        half = sums // 2
        @cache
        def helper(idx: int, sum1: int, sum2: int) -> int:
            if idx == n:
                return sum1 == sum2
            
            if sum1 > half or sum2 > half:
                return False
            
            return helper(idx + 1, sum1 + nums[idx], sum2) or helper(idx + 1, sum1, sum2 + nums[idx])
        return helper(0, 0, 0)
    
    def canPartition4(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        sums, half = sum(nums), sum(nums) // 2
        if sums % 2 != 0:
            return False
        arr, n = [0] * 2, len(nums)
        @cache
        def helper(idx: int, arr: tuple):
            if idx == n:
                return all(arr[i] == half for i in range(2))
            arr = list(arr)
            for i in range(2):
                if arr[i] + nums[idx] > half:
                    continue
                arr[i] += nums[idx]
                if helper(idx + 1, tuple(arr)):
                    return True
                arr[i] -= nums[idx]
            return False
        return helper(0, tuple([0] * 2))