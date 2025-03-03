class Solution:
    """
    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).

    Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    Example 2:

    Input: s = "aa", p = "*"
    Output: true
    Explanation: '*' matches any sequence.
    Example 3:

    Input: s = "cb", p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
    """
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        
        m, n = len(s), len(p)
        @cache
        def helper(idx1: int, idx2: int) -> int:
            if idx1 == m and idx2 == n:
                return True
            
            if idx1 > m:
                return False
            
            if idx1 < m and idx2 < n and s[idx1] == p[idx2]:
                return helper(idx1 + 1, idx2 + 1)
            
            if idx2 < n and p[idx2] == '*':
                return helper(idx1 + 1, idx2) or helper(idx1 + 1, idx2 + 1) or helper(idx1, idx2 + 1)
            elif idx1 < m and idx2 < n and p[idx2] == '?':
                return helper(idx1 + 1, idx2 + 1)
            return False

        return helper(0, 0)
        