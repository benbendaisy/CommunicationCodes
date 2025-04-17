class Solution:
    """
    A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

    For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
    Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

    A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

    Example 1:

    Input: n = 1
    Output: 5
    Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
    Example 2:

    Input: n = 4
    Output: 400
    Example 3:

    Input: n = 50
    Output: 564908303
    """
    def countGoodNumbers1(self, n: int) -> int:
        mod = 10 ** 9 + 7
        
        @cache
        def helper(pos: int) -> int:
            if pos == n:
                return 1
            if pos % 2 == 0:
                choices = 5  # Even index → even digit: 0,2,4,6,8
            else:
                choices = 4  # Odd index → prime digit: 2,3,5,7
            return (choices * helper(pos + 1)) % mod
        
        return helper(0)
    
    def countGoodNumbers2(self, n: int) -> int:
        MOD = 10**9 + 7
        even_positions = (n + 1) // 2  # 0-based even indices: 0, 2, 4, ...
        odd_positions = n // 2         # 0-based odd indices: 1, 3, 5, ...
        return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD