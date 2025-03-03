class Solution:
    """
    Given two strings s and t, return the number of distinct subsequences of s which equals t.

    The test cases are generated so that the answer fits on a 32-bit signed integer.

    Example 1:

    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
    As shown below, there are 3 ways you can generate "rabbit" from s.
    rabbbit
    rabbbit
    rabbbit
    Example 2:

    Input: s = "babgbag", t = "bag"
    Output: 5
    Explanation:
    As shown below, there are 5 ways you can generate "bag" from s.
    babgbag
    babgbag
    babgbag
    babgbag
    babgbag
    """
    def numDistinct1(self, s: str, t: str) -> int:
        """
        Time Limit Exceeded
        """
        if not s and not t:
            return 1
        elif not s or not t or len(s) < len(t):
            return 0
        
        m, n = len(s), len(t)
        @cache
        def helper(idx1: int, idx2: int) -> int:
            if idx1 == m:
                return 1 if idx2 == n else 0
            
            if idx2 == n:
                return 1
            
            cnt = 0
            for i in range(idx1, m):
                if s[i] == t[idx2]:
                    cnt += helper(i + 1, idx2 + 1)
            return cnt
        
        return helper(0, 0)
    
    def numDistinct(self, s: str, t: str) -> int:
        if not s and not t:
            return 1
        elif not s or not t or len(s) < len(t):
            return 0
        
        m, n = len(s), len(t)

        @cache
        def helper(idx1: int, idx2: int) -> int:
            if idx2 == n:
                return 1
            
            if idx1 == m:
                return 0
            
            if s[idx1] == t[idx2]:
                return helper(idx1 + 1, idx2 + 1) + helper(idx1 + 1, idx2)
            
            return helper(idx1 + 1, idx2)
        
        return helper(0, 0)