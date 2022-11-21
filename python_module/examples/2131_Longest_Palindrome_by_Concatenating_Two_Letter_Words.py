from collections import Counter
from typing import List


class Solution:
    """

    """
    def longestPalindrome(self, words: List[str]) -> int:
        wordDict = Counter(words)
        ans = 0
        center = False
        for word, cnt in wordDict.items():
            if word[0] == word[1]:
                if cnt % 2 == 0:
                    ans += cnt
                else:
                    ans += cnt - 1
                    center = True
            # consider a pair of non-palindrome words,
            # such that one is the reverse of another
            # word[::-1] is the reversed word
            elif word[0] < word[1]:
                ans += 2 * min(cnt, wordDict[word[::-1]])
        if center:
            ans += 1       # to make the result +2
        return 2 * ans
