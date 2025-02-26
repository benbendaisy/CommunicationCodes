from functools import lru_cache
from typing import List


class Solution:
    """
        Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

        answer[i] % answer[j] == 0, or
        answer[j] % answer[i] == 0
        If there are multiple solutions, return any of them.

        Example 1:

        Input: nums = [1,2,3]
        Output: [1,2]
        Explanation: [1,3] is also accepted.
        Example 2:

        Input: nums = [1,2,4,8]
        Output: [1,2,4,8]

        Constraints:

        1 <= nums.length <= 1000
        1 <= nums[i] <= 2 * 109
        All the integers in nums are unique.
    """
    def largestDivisibleSubset1(self, nums: List[int]) -> List[int]:
        @lru_cache(None)
        def ends(idx):
            maxSet = []
            for p in range(idx):
                if nums[idx] % nums[p] == 0:
                    sub = ends(p)
                    if len(sub) > len(maxSet):
                        maxSet = sub

            return maxSet + [nums[idx]]

        if len(nums) == 0:
            return []
        nums.sort()
        return max([ends(i) for i in range(len(nums))], key=len)
    
    def largestDivisibleSubset2(self, nums: List[int]) -> List[int]:
        @cache
        def helper(idx):
            tail = nums[idx]
            max_subset = []
            for p in range(idx):
                if tail % nums[p] == 0:
                    subset = helper(p)
                    if len(max_subset) < len(subset):
                        max_subset = subset
            max_subset = max_subset.copy()
            max_subset.append(tail)
            return max_subset
        if len(nums) == 0:
            return []
        nums.sort()
        return max([helper(i) for i in range(len(nums))], key=len)

    def largestDivisibleSubset3(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        
        n = len(nums)
        nums.sort()
        dp = [[num] for num in nums]
        max_idx = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(dp[max_idx]):
                max_idx = i
        return dp[max_idx]
    
    def largestDivisibleSubset4(self, nums: List[int]) -> List[int]:
        """
        TLE: back stracking
        """
        if not nums:
            return 0

        n = len(nums)
        nums.sort()
        
        dp = []
        def helper(path: List[int], idx: int):
            if path:
                dp.append(path)
            
            if idx == n:
                return
            
            for i in range(idx, n):
                if not path or nums[i] % path[-1] == 0:
                    helper(path + [nums[i]], i + 1)
        helper([], 0)
        return max(dp, key=len)
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        @cache
        def helper(idx: int):
            max_subset = []
            for i in range(idx):
                if nums[idx] % nums[i] == 0:
                    subset = helper(i)
                    if len(max_subset) < len(subset):
                        max_subset = subset
            return max_subset + [nums[idx]]
        return max([helper(i) for i in range(len(nums))], key=len)