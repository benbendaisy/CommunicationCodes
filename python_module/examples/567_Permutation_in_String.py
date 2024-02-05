class Solution:
    """
        Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

        In other words, return true if one of s1's permutations is the substring of s2.

        Example 1:

        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").
        Example 2:

        Input: s1 = "ab", s2 = "eidboaoo"
        Output: false
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = [0] * 26
        for ch in s1:
            dict_s1[ord(ch) - ord('a')] += 1
        n1, n2 = len(s1), len(s2)
        for i in range(n2 - n1 + 1):
            dict_s2 = [0] * 26
            for j in range(i, i + n1):
                dict_s2[ord(s2[j]) - ord('a')] += 1
            if dict_s1 == dict_s2:
                return True
        return False