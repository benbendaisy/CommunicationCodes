class Solution:
    """
    There is a strange printer with the following two special properties:

    The printer can only print a sequence of the same character each time.
    At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
    Given a string s, return the minimum number of turns the printer needed to print it.

    Example 1:

    Input: s = "aaabbb"
    Output: 2
    Explanation: Print "aaa" first and then print "bbb".
    Example 2:

    Input: s = "aba"
    Output: 2
    Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
    """
    def strangePrinter1(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def helper(left, right):
            if left >= right: 
                return 0
            best = helper(left + 1, right) + 1
            for idx in range(left + 1, right + 1):
                if s[left] == s[idx]:
                    best = min(best, helper(left, idx - 1) + helper(idx, right))
            return best
        return helper(0, n - 1) + 1
    
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        dp = [[sys.maxsize] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for j in range(2, n + 1):
            for i in range(n - j + 1):
                k = i + j - 1
                dp[i][k] = dp[i + 1][k] + 1
                for l in range(i + 1, k + 1):
                    if s[i] == s[l]:
                        dp[i][k] = min(dp[i][k], dp[i][l - 1] + +(dp[l + 1][k] if k > l else 0))
        return dp[0][n - 1]