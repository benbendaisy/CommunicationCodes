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
    
    def largestDivisibleSubset5(self, nums: List[int]) -> List[int]:
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
    
    def largestDivisibleSubset6(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Sort the array to ensure the divisibility condition is easier to check.
        nums.sort()
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def helper(idx: int, prev_idx: int) -> List[int]:
            # prev_idx is -1 if no element has been chosen yet.
            best_subset = []
            
            # Iterate through the remaining elements.
            for i in range(idx, n):
                # Check divisibility condition if an element has been chosen.
                if prev_idx == -1 or nums[i] % nums[prev_idx] == 0:
                    candidate = helper(i + 1, i)
                    # Update best_subset if we found a longer valid subset.
                    if len(candidate) > len(best_subset):
                        best_subset = candidate
            
            # If an element has been chosen, include it at the beginning.
            return ([nums[prev_idx]] + best_subset) if prev_idx != -1 else best_subset
        
        # Start with idx 0 and no previous element (denoted by -1).
        return helper(0, -1)
    
    def largestDivisibleSubset7(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        @cache
        def helper(idx: int, prev: int):
            best = []
            for i in range(idx, n):
                if prev == -1 or nums[i] % nums[prev] == 0:
                    candidate = helper(i + 1, i)
                    if len(candidate) > len(best):
                        best = candidate
            return [nums[prev]] + best if prev != -1 else best
        return helper(0, -1)
    
    def largestDivisibleSubset8(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n, self.res = len(nums), []
        @cache
        def helper(idx: int, path: tuple):
            if len(self.res) < len(path):
                self.res = list(path)
                
            for i in range(idx, n):
                if not path or nums[i] % path[-1] == 0:
                    helper(i + 1, path + (nums[i],))
        helper(0, ())
        return self.res