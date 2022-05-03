import math
from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if not wordsDict or not word1 or not word2:
            return -1

        locs1 = [x for x in range(len(wordsDict)) if wordsDict[x] == word1]
        locs2 = [x for x in range(len(wordsDict)) if wordsDict[x] == word2]

        l1 = l2 = 0
        minDist = math.inf
        while l1 < len(locs1) and l2 < len(locs2):
            loc1, loc2 = locs1[l1], locs2[l2]
            if locs1[l1] != locs2[l2]:
                minDist = min(minDist, abs(loc1, loc2))

            if loc1 < loc2:
                l1 += 1
            else:
                l2 += 1

        return minDist

if __name__ == "__main__":
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "coding"
    solution = Solution()
    ret = solution.shortestWordDistance(wordsDict, word1, word2)
    print(ret)