from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return False

        strCntMap = defaultdict(int)

        for ch in s:
            strCntMap[ch] += 1

        oddCnt = 0
        for key, value in strCntMap.items():
            if value % 2 != 0:
                oddCnt += 1

        return False if oddCnt > 1 else True