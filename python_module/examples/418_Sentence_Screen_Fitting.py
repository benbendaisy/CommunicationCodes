from functools import lru_cache
from typing import List


class Solution:
    """
        Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

        The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

        Example 1:

        Input: sentence = ["hello","world"], rows = 2, cols = 8
        Output: 1
        Explanation:
        hello---
        world---
        The character '-' signifies an empty space on the screen.
        Example 2:

        Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
        Output: 2
        Explanation:
        a-bcd-
        e-a---
        bcd-e-
        The character '-' signifies an empty space on the screen.
        Example 3:

        Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
        Output: 1
        Explanation:
        i-had
        apple
        pie-i
        had--
        The character '-' signifies an empty space on the screen.
    """
    def wordsTyping1(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        ans = 0
        idx = 0
        for _ in range(rows):
            c = 0
            while c + len(sentence[idx]) <= cols:
                c += len(sentence[idx]) + 1
                idx += 1
                if idx == n:
                    ans += 1
                    idx = 0
        return ans

    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)

        @lru_cache(None)
        def dfs(idx):
            # Return (nextIndex, times) if the word at ith is the beginning of the row
            c = 0
            times = 0
            while c + len(sentence[idx]) <= cols:
                c += len(sentence[idx]) + 1
                idx += 1
                if idx == n:
                    times += 1
                    idx = 0
            return idx, times

        ans = 0
        idx = 0
        for _ in range(rows):
            idx, times = dfs(idx)
            ans += times
        return ans