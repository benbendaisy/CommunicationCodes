from collections import defaultdict


class Solution:
    def canConstruct1(self, s: str, k: int) -> bool:
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
    
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        char_dict = defaultdict(int)
        for ch in s:
            char_dict[ch] += 1
        odd = 0
        for _, val in char_dict.items():
            if val % 2 != 0:
                odd += 1
        return odd <= k