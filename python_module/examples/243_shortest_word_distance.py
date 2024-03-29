import math
import sys
from typing import List


class Solution:
    def shortestDistance1(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if not wordsDict or not word1 or not word2:
            return -1
        arr = [1 if word1 == x else 0 for x in wordsDict]
        min_dist = sys.maxsize
        for i in range(len(wordsDict)):
            if word2 == wordsDict[i]:
                left = right = i

                while left >= 0 and arr[left] != 1:
                    left -= 1
                if left >= 0 and arr[left] == 1:
                    min_dist = min(min_dist, i - left)

                while right < len(wordsDict) and arr[right] != 1:
                    right += 1
                if right < len(wordsDict) and arr[right] == 1:
                    min_dist = min(min_dist, right - i)

        return min_dist

    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if not wordsDict or not word1 or not word2:
            return -1

        word1Dist = [x for x in range(len(wordsDict)) if wordsDict[x] == word1]
        word2Dist = [x for x in range(len(wordsDict)) if wordsDict[x] == word2]

        minDist = math.inf
        for x in word1Dist:
            for y in word2Dist:
                minDist = min(minDist, abs(x - y))
        return minDist


if __name__ == "__main__":
    arr = ["practice", "makes", "perfect", "coding", "makes"]
    solution = Solution()
    ret = solution.shortestDistance(arr, "coding", "practice")
    print(ret)
