from collections import Counter
from typing import List


class Solution:
    """
    You are given an array of strings words. Each element of words consists of two lowercase English letters.

    Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

    Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

    A palindrome is a string that reads the same forward and backward.

    Example 1:

    Input: words = ["lc","cl","gg"]
    Output: 6
    Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
    Note that "clgglc" is another longest palindrome that can be created.
    Example 2:

    Input: words = ["ab","ty","yt","lc","cl","ab"]
    Output: 8
    Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
    Note that "lcyttycl" is another longest palindrome that can be created.
    Example 3:

    Input: words = ["cc","ll","xx"]
    Output: 2
    Explanation: One longest palindrome is "cc", of length 2.
    Note that "ll" is another longest palindrome that can be created, and so is "xx".
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
