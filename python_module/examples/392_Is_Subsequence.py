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

    def isSubsequence(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        idx_s, idx_t = 0, 0
        while idx_s < ls and idx_t < lt:
            if s[idx_s] == t[idx_t]:
                idx_s += 1
                idx_t += 1
            else:
                idx_t += 1
        return idx_s == ls

