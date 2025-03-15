class Solution:
    """
        The Tribonacci sequence Tn is defined as follows:

        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

        Given n, return the value of Tn.

        Example 1:

        Input: n = 4
        Output: 4
        Explanation:
        T_3 = 0 + 1 + 1 = 2
        T_4 = 1 + 1 + 2 = 4
        Example 2:

        Input: n = 25
        Output: 1389537
    """
    @lru_cache(None)
    def tribonacci1(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
    
    @cache
    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

    @cache
    def tribonacci3(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
    
    @cache
    def tribonacci(self, n: int) -> int:
        @cache
        def helper(m: int) -> int:
            if m == 0: return 0
            if m == 1: return 1
            if m == 2: return 1

            return helper(m - 1) + helper(m - 2) + helper(m - 3)
        return helper(n)
    
