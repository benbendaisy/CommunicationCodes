import math
from collections import defaultdict
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dictStore = defaultdict(lambda : [])
        for i in range(len(wordsDict)):
            self.dictStore[wordsDict[i]].append(i)

    def shortest1(self, word1: str, word2: str) -> int:
        if word1 not in self.dictStore or word2 not in self.dictStore:
            return None
        minDist = math.inf
        for i in self.dictStore[word1]:
            for j in self.dictStore[word2]:
                minDist = min(minDist, abs(i - j))
        return minDist

    def shortest(self, word1: str, word2: str) -> int:
        if word1 not in self.dictStore or word2 not in self.dictStore:
            return None

        l1 = l2 = 0
        minDist = math.inf
        while l1 < len(self.dictStore[word1]) and l2 < len(self.dictStore[word2]):
            loc1, loc2 = self.dictStore[word1][l1], self.dictStore[word2][l2]
            minDist = min(minDist, abs(loc1 - loc2))

            if loc1 < loc2:
                l1 += 1
            else:
                l2 += 1
        return minDist