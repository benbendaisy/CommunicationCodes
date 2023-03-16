class Solution:
    """
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Example 1:

        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0
        Explanation: "sad" occurs at index 0 and 6.
        The first occurrence is at index 0, so we return 0.
        Example 2:

        Input: haystack = "leetcode", needle = "leeto"
        Output: -1
        Explanation: "leeto" did not occur in "leetcode", so we return -1.
    """
    def strStr1(self, haystack: str, needle: str) -> int:
        if not haystack or not needle or len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            found = True
            for j in range(len(needle)):
                if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)
        if m == 0:
            return 0
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[j] != needle[i]:
                j = pi[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            pi[i] = j
        j = 0
        for i in range(n):
            while j > 0 and needle[j] != haystack[i]:
                j = pi[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            if j == m:
                return i - m + 1
        return -1