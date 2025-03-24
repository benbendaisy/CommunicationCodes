class Solution:
    """
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

        Example 1:

        Input: s = "abc", t = "ahbgdc"
        Output: true
        Example 2:

        Input: s = "axc", t = "ahbgdc"
        Output: false

        Constraints:

        0 <= s.length <= 100
        0 <= t.length <= 104
        s and t consist only of lowercase English letters.
    """

    def isSubsequence1(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        idx_s, idx_t = 0, 0
        while idx_s < ls and idx_t < lt:
            if s[idx_s] == t[idx_t]:
                idx_s += 1
                idx_t += 1
            else:
                idx_t += 1
        return idx_s == ls
    
    def isSubsequence2(self, s: str, t: str) -> bool:
        if not s:
            return True  # An empty string is always a subsequence
        
        m, n = len(s), len(t)
        
        @lru_cache(None)
        def helper(i: int, j: int) -> bool:
            if i == m:  
                return True  # Found all characters in `s` within `t`
            if j == n:  
                return False  # Reached the end of `t` without fully matching `s`
            
            if s[i] == t[j]:  
                return helper(i + 1, j + 1)  # Move both pointers if characters match
            
            return helper(i, j + 1)  # Otherwise, move only `t` pointer

        return helper(0, 0)
    
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        m, n = len(s), len(t)
        @cache
        def helper(idx: int, sub_seq: str) -> bool:
            if sub_seq == s:
                return True
            if idx == n or len(sub_seq) >= m:
                return False
            
            
            for i in range(idx, n):
                if helper(i + 1, sub_seq + t[i]):
                    return True
            return False
        return helper(0, "")

