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

    def integerBreak2(self, n: int) -> int:
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
    
    def integerBreak3(self, n: int) -> int:
        factors = [i for i in range(1, n)]
        max_product = float('-inf')
        @cache
        def helper(sums: int, product: int):
            nonlocal max_product
            if sums == n:
                max_product = max(max_product, product)
                return
            
            for i in range(len(factors)):
                t = sums + factors[i]
                if t <= n:
                    helper(t, product * factors[i])
        helper(0, 1)    
        return max_product
    
    def integerBreak4(self, n: int) -> int:
        if n <= 3:
            return n - 1
        @cache
        def helper(num: int):
            if num <= 3:
                return num
            max_product = num
            for i in range(2, num):
                max_product = max(max_product, i * helper(num - i))
            return max_product
        return helper(n)
    
    def integerBreak5(self, n: int) -> int:
        @cache
        def helper(remaining: int, product: int, step: int) -> int:
            if remaining == 0:
                if step >= 2:
                    return product
                return 0
            max_prod = float('-inf')
            for i in range(1, remaining + 1):
                max_prod = max(max_prod, helper(remaining - i, product * i, step + 1))
            return max_prod
        
        return helper(n, 1, 0)
    
    def integerBreak(self, n: int) -> int:
        @cache
        def helper(remaining: int, product: int, steps: int):
            if remaining == 0:
                if steps >= 2:
                    return product
                return 0
            
            max_product = float('-inf')
            for i in range(1, remaining + 1):
                max_product = max(max_product, helper(remaining - i, product * i, steps + 1))
            return max_product
        return helper(n, 1, 0)