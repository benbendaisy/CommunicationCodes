from collections import defaultdict
from typing import List


class Solution:
    def countCharacterChanges(self, s:str):
        charsMap = defaultdict(int)
        for ch in s:
            charsMap[ch] += 1
        cnt = 0
        for value in charsMap.values():
            if value % 2 == 1:
                cnt += 1
        return cnt // 2

    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        if not queries:
            return []
        arr = []
        for left, right, k in queries:
            res = self.countCharacterChanges(s[left: right + 1]) <= k
            arr.append(res)
        return arr

