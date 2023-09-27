class Solution:
    """
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

    Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    Example 2:

    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    Example 3:

    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
    """
    def isMatch1(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
            else:
                dp[0][j] = j > 1 and p[j - 2] == '*' and dp[0][j-2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (p[j-2] == s[i-1] or p[j-2] == '.') and dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[m][n]

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        @lru_cache(None)
        def is_match(idx_s, idx_p):
            if idx_p == n:
                return idx_s == m
            first_match = idx_s < m and (p[idx_p] == s[idx_s] or p[idx_p] == '.')
            if idx_p + 1 < n and p[idx_p + 1] == '*':
                ans = is_match(idx_s, idx_p + 2) or (first_match and is_match(idx_s + 1, idx_p))
            else:
                ans = first_match and is_match(idx_s + 1, idx_p + 1)
            return ans
        return is_match(0, 0)