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
    
    def jump3(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0
        for i, _ in enumerate(nums):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
    
    def jump4(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n <= 1:
            return 0
        
        @cache
        def helper(position: int):
            # If we're at or beyond the last position, we're done
            if position >= n - 1:
                return 0
            
            # Initialize min_jumps to infinity
            min_jumps = float('inf')
            
            # Try all possible jumps from current position
            max_jump = min(position + nums[position], n - 1)
            for next_pos in range(position + 1, max_jump + 1):
                min_jumps = min(min_jumps, 1 + helper(next_pos))
                
            return min_jumps
        
        # Start from position 0
        result = helper(0)
        return result if result != float('inf') else -1
    

    def jump5(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return 0
        @cache # Memoization to avoid redundant calculations
        def helper(idx: int):
            if idx >= n - 1: # Base case: reached or exceeded last index
                return 0
            min_jumps = float('inf')
            for i in range(1, nums[idx] + 1): # Try all jumps within range
                if i + idx < n: # Ensure we don't go out of bounds
                    min_jumps = min(min_jumps, 1 + helper(i + idx))
            return min_jumps

        return helper(0)
    
    def jump6(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        @cache
        def helper(idx: int) -> int:
            if idx >= n - 1:
                return 0  # No jumps needed if at or beyond last index
            
            min_jumps = float('inf')
            max_jump = nums[idx]  # Maximum jump length from current position
            
            for i in range(1, max_jump + 1):
                if idx + i < n:
                    min_jumps = min(min_jumps, 1 + helper(idx + i))
            
            return min_jumps
        
        return helper(0)
    
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        @cache
        def helper(idx: int) -> int:
            if idx >= n - 1:
                return 0
            
            min_jumps = float('inf')
            for i in range(1, nums[idx] + 1):
                min_jumps = min(min_jumps, 1 + helper(idx + i))
            return min_jumps
        return helper(0)