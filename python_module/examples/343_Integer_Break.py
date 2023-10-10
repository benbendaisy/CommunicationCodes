class Solution:
    """
        Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

        Return the maximum product you can get.

        Example 1:

        Input: n = 2
        Output: 1
        Explanation: 2 = 1 + 1, 1 × 1 = 1.
        Example 2:

        Input: n = 10
        Output: 36
        Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

        Constraints:

        2 <= n <= 58
    """
    def integerBreak1(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(j * (i-j), j * dp[i-j], dp[i])
        return dp[-1]

    def integerBreak(self, n: int) -> int:
        @cache
        def dp(num):
            if num <= 3:
                return num
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))
            return ans
        if n <= 3:
            return n - 1
        return dp(n)