from functools import lru_cache


class Solution:
    def __init__(self):
        self.palSet = set()

    def countPalindromicSubsequences1(self, s: str) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def countPalSub(str1: str):
            if not str1:
                return
            elif len(str1) == 1:
                self.palSet.add(str1)
                return
            elif str1 == str1[::-1]:
                self.palSet.add(str1)

            for i in range(len(str1)):
                countPalSub(str1[:i] + str1[i + 1:])

        countPalSub(s)
        return len(self.palSet) % mod

    def countPalindromicSubsequences(self, s: str) -> int:
        resSet = set()
        def palindromicSubs(str1, str2):
            if len(str1) == 0:
                if str2 and str2 == str2[::-1]:
                    resSet.add(str2)
                return
            palindromicSubs(str1[1:], str2 + str1[0])
            palindromicSubs(str1[1:], str2)

        palindromicSubs(s, "")
        return len(resSet)
