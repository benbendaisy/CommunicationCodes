from typing import List


class Solution:
    """
        You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

        If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

        Return the maximum coins you can collect by bursting the balloons wisely.

        Example 1:

        Input: nums = [3,1,5,8]
        Output: 167
        Explanation:
        nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
        coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
        Example 2:

        Input: nums = [1,5]
        Output: 10

        Constraints:

        n == nums.length
        1 <= n <= 300
        0 <= nums[i] <= 100
    """
    def __init__(self):
        self.memoDict = dict()
    def maxCoins1(self, nums: List[int]) -> int:
        if tuple(nums) in self.memoDict:
            return self.memoDict[tuple(nums)]
        if len(nums) == 1:
            return nums[0]
        maxCoin = 0
        for i in range(len(nums)):
            a = 1 if i == 0 else nums[i - 1]
            b = 1 if i == len(nums) - 1 else nums[i + 1]
            t = a * b * nums[i]
            maxCoin = max(maxCoin, t + self.maxCoins(nums[:i] + nums[i + 1:]))
        self.memoDict[tuple(nums)] = maxCoin
        return maxCoin
    
    def maxCoins2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Add boundary 1s to simplify computation
        nums = [1] + nums + [1]
        
        @cache
        def helper(arr: tuple) -> int:
            if len(arr) == 2:  # Only boundary values remain
                return 0
            
            max_coin = 0
            for i in range(1, len(arr) - 1):  # Avoid the artificial boundaries
                coins = arr[i - 1] * arr[i] * arr[i + 1]  # Burst balloon i
                new_arr = arr[:i] + arr[i + 1:]  # Remove the balloon
                max_coin = max(max_coin, coins + helper(new_arr))
            
            return max_coin
        
        return helper(tuple(nums))
    
    def maxCoins3(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Add boundary 1s to simplify computation
        nums = [1] + nums + [1]
        @cache
        def helper(arr: tuple) -> int:
            # Only boundary values remain
            if len(arr) == 2:
                return 0
            
            n = len(arr)
            max_coin = 0
             # Avoid the artificial boundaries
            for i in range(1, n - 1):
                # Burst balloon i
                coins = arr[i - 1] * arr[i] * arr[i + 1]
                # Remove the balloon
                new_arr = arr[:i] + arr[i + 1:]
                max_coin = max(max_coin, coins + helper(new_arr))
            return max_coin
        return helper(tuple(nums))
    
    def maxCoins4(self, nums: List[int]) -> int:
        # Add boundary balloons
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Create memoization table
        @cache
        def dp(left, right):
            # If there are no balloons between left and right boundaries
            if left + 1 >= right:
                return 0
            
            # Find maximum coins by trying each balloon as the last to burst
            max_coins = 0
            for i in range(left + 1, right):
                # Current balloon burst value
                curr = nums[left] * nums[i] * nums[right]
                
                # Recursive subproblems for remaining balloons
                left_subproblem = dp(left, i)
                right_subproblem = dp(i, right)
                
                # Update maximum
                max_coins = max(max_coins, curr + left_subproblem + right_subproblem)
                
            return max_coins
        
        # Solve the problem for the entire array
        return dp(0, n - 1)
    
    def maxCoins(self, nums: List[int]) -> int:
        # Add boundary balloons
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Create memoization table
        @cache
        def helper(left: int, right: int) -> int:
            if left + 1 >= right:
                return 0
            
            max_coins = 0
            for i in range(left + 1, right):
                cur = nums[left] * nums[i] * nums[right]
                left_sub = helper(left, i)
                right_sub = helper(i, right)
                max_coins = max(max_coins, cur + left_sub + right_sub)
            return max_coins
        
        return helper(0, n - 1)

