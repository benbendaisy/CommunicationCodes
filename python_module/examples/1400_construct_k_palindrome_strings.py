from collections import defaultdict


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if not s:
            return True
        elif len(s) < k:
            return False

        charDict = defaultdict(int)
        for ch in s:
            charDict[ch] += 1
        cnt = 0
        for value in charDict.values():
            if value % 2 == 1:
                cnt += 1

        return 1 if cnt <= k else 0