from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        arr = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue

                concatedStr = word1 + word2
                if concatedStr == concatedStr[::-1]:
                    arr.append([i, j])
        return arr