from collections import Counter


class Solution:
    """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

        Example 1:

        Input: s = "anagram", t = "nagaram"
        Output: true
        Example 2:

        Input: s = "rat", t = "car"
        Output: false

        Constraints:

        1 <= s.length, t.length <= 5 * 104
        s and t consist of lowercase English letters.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        chDict = Counter(s)

        for ch in t:
            if ch not in chDict:
                return False
            chDict[ch] -= 1

        for k, v in chDict.items():
            if v != 0:
                return False

        return True