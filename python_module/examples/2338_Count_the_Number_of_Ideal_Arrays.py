class Solution:
    """
    You are given two integers n and maxValue, which are used to describe an ideal array.

    A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

    Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
    Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
    Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

    Example 1:

    Input: n = 2, maxValue = 5
    Output: 10
    Explanation: The following are the possible ideal arrays:
    - Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
    - Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
    - Arrays starting with the value 3 (1 array): [3,3]
    - Arrays starting with the value 4 (1 array): [4,4]
    - Arrays starting with the value 5 (1 array): [5,5]
    There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
    Example 2:

    Input: n = 5, maxValue = 3
    Output: 11
    Explanation: The following are the possible ideal arrays:
    - Arrays starting with the value 1 (9 arrays): 
    - With no other distinct values (1 array): [1,1,1,1,1] 
    - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
    - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
    - Arrays starting with the value 2 (1 array): [2,2,2,2,2]
    - Arrays starting with the value 3 (1 array): [3,3,3,3,3]
    There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
    """
    def idealArrays1(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(length_left, prev):
            if length_left == 0:
                return 1
            total = 0
            multiple = prev
            while multiple <= maxValue:
                total = (total + dfs(length_left - 1, multiple)) % MOD
                multiple += prev
            return total

        # Try all possible starting values
        result = 0
        for start in range(1, maxValue + 1):
            result = (result + dfs(n - 1, start)) % MOD
        return result
    
    def idealArrays2(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        from math import comb

        # Precompute number of ways to form array of length k ending at val
        # Using combinatorics: for a sequence of length `n` with `k` distinct elements
        # the number of such sequences is comb(n - 1, k - 1)
        max_k = min(n, 14)  # max depth of divisor chain; 14 is a safe upper bound

        # dp[k][val] = number of sequences of length k ending with val
        dp = [ [0] * (maxValue + 1) for _ in range(max_k + 1) ]
        
        for val in range(1, maxValue + 1):
            dp[1][val] = 1
        
        for k in range(2, max_k + 1):
            for val in range(1, maxValue + 1):
                for mult in range(2 * val, maxValue + 1, val):
                    dp[k][mult] = (dp[k][mult] + dp[k - 1][val]) % MOD

        # Sum over all possible lengths `k` and all values, weighted by comb(n-1, k-1)
        result = 0
        for k in range(1, max_k + 1):
            coeff = comb(n - 1, k - 1)
            for val in range(1, maxValue + 1):
                result = (result + dp[k][val] * coeff) % MOD

        return result