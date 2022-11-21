from functools import lru_cache
from string import ascii_lowercase


class Solution:
    """
        You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

        We repeatedly make duplicate removals on s until we no longer can.

        Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

        Example 1:

        Input: s = "abbaca"
        Output: "ca"
        Explanation:
        For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
        Example 2:

        Input: s = "azxxzy"
        Output: "ay"
    """
    def removeDuplicates1(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        n = len(s)
        l = 1
        while l < n:
            if s[l] == s[l - 1]:
                return self.removeDuplicates1(s[:l-1] + s[l + 1:])
            l += 1
        return s

    def removeDuplicates2(self, s: str) -> str:
        res = []
        for ch in s:
            if res and ch == res[-1]:
                res.pop()
            else:
                res.append(ch)
        return "".join(res)

    def removeDuplicates(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        duplicates = {2 * ch for ch in ascii_lowercase}
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for du in duplicates:
                s = s.replace(du, "")
        return s

