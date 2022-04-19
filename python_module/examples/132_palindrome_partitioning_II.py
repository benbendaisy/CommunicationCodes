import functools
from collections import defaultdict
from typing import List


class Solution:
    def minCut1(self, s: str) -> int:
        n = len(s)
        if not s or n == 1:
            return 0
        if n == 2:
            return 0 if s[0] == s[1] else 1

        cut = n
        if s[0] == s[n - 1]:
            cut = self.minCut(s[1 : n - 1])
        else:
            cut = 1 + min(self.minCut(s[1 :]), self.minCut(s[: n - 1]))

        return cut

    def minCutWithCache(self, s: str, memory: List):
        length = len(s)
        if length <= 1:
            return 0
        elif length == 2:
            return 0 if s[0] == s[1] else 1
        elif memory[s] >= 0:
            return memory[s]
        elif s == s[::-1]:
            memory[s] = 0
            return 0

        cut = length
        for i in range(1, length):
            st = s[:i]
            if st == st[::-1]:
                cut = min(cut, 1 + self.minCutWithCache(s[i:], memory))
        memory[s] = cut
        return cut

    def minCut(self, s: str) -> int:
        memory = defaultdict(lambda:-1)
        return self.minCutWithCache(s, memory)

if __name__ == "__main__":
    s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
    solution = Solution()
    ret = solution.minCut(s)
    print(ret)