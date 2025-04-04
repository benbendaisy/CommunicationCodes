class Solution:
    """
    Given an integer n, return the number of trailing zeroes in n!.

    Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

    Example 1:

    Input: n = 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.
    Example 2:

    Input: n = 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.
    Example 3:

    Input: n = 0
    Output: 0
    """
    def trailingZeroes(self, n: int) -> int:
        def helper(k: int) -> int:
            if n == 0:
                return 0
            cnt = 0
            for i in range(1, n + 1):
                m = i
                while m % k == 0:
                    cnt += 1
                    m //= k
            return cnt
        
        cnt_2 = helper(2)
        cnt_5 = helper(5)
        return min(cnt_2, cnt_5)