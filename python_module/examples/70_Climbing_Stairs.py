from functools import lru_cache


class Solution:
    """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Example 1:

        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
        Example 2:

        Input: n = 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
    """
    @lru_cache(None)
    def climbStairs1(self, n: int) -> int:
        if n <= 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [1] * n
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
    
    @cache
    def climbStairs3(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) 
    
    @cache
    def climbStairs4(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    @cache
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(m: int) -> int:
            if m == 1: return 1
            if m == 2: return 2
            return helper(m - 1) + helper(m - 2)
        
        return helper(n)
