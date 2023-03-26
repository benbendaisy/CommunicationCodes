from collections import defaultdict


class Solution:
    """
        We define the string base to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so base will look like this:

        "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
        Given a string s, return the number of unique non-empty substrings of s are present in base.

        Example 1:

        Input: s = "a"
        Output: 1
        Explanation: Only the substring "a" of s is in base.
        Example 2:

        Input: s = "cac"
        Output: 2
        Explanation: There are two substrings ("a", "c") of s in base.
        Example 3:

        Input: s = "zab"
        Output: 6
        Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of s in base.
    """
    def findSubstringInWraproundString1(self, s: str) -> int:
        left = 0
        d = defaultdict(int)
        for right, ch in enumerate(s):
            if right == 0:
                d[ch] = 1
                prev = ch
                continue
            if not (ord(ch) - ord(prev) == 1) and not (ord(prev) - ord(ch)) == 25:
                left = right

            d[ch] = max(d[ch], right - left + 1)
            prev = ch
        return sum(d.values())

    def findSubstringInWraproundString(self, s: str) -> int:
        d = defaultdict(int)
        streak = 0
        for i in range(len(s)):
            streak = streak + 1 if (ord(s[i - 1]) - 96) % 26 == (ord(s[i]) - 97) else 1
            d[s[i]] = max(d[s[i]], streak)
        return sum(d.values())

