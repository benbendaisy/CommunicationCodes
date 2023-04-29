from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    """
        You are given a list of strings of the same length words and a string target.

        Your task is to form target using the given words under the following rules:

        target should be formed from left to right.
        To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
        Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
        Repeat the process until you form the string target.
        Notice that you can use multiple characters from the same string in words provided the conditions above are met.

        Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

        Example 1:

        Input: words = ["acca","bbbb","caca"], target = "aba"
        Output: 6
        Explanation: There are 6 ways to form target.
        "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
        "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
        "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
        "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
        "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
        "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
        Example 2:

        Input: words = ["abba","baab"], target = "bab"
        Output: 4
        Explanation: There are 4 ways to form target.
        "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
        "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
        "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
        "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
    """
    def numWays1(self, words: List[str], target: str) -> int:
        if not words:
            return 0
        m, n = len(words[0]), len(target)
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        counter = [[0] * 26 for _ in range(m)]
        for i in range(m):
            for word in words:
                counter[i][ord(word[i]) - ord('a')] += 1

        for i in range(m):
            for j in range(n - 1, -1, -1):
                dp[j + 1] += dp[j] * counter[i][ord(target[j]) - ord('a')]
                dp[j + 1] %= mod
        return dp[n]

    def numWays(self, words: List[str], target: str) -> int:
        cols = list(map(Counter, zip(*words)))
        m, n = len(words[0]), len(target)

        @lru_cache(None)
        def dp(i, j): #i: idx of target, j: idx of cols
            # str formed
            if i == n:
                return 1
            elif m - j < n - i: # impossible to form str
                return 0
            # not use / use a letter from this column
            return dp(i, j + 1) + cols[j][target[i]] * dp(i + 1, j + 1)
        return dp(0, 0) % (10 ** 9 + 7)
