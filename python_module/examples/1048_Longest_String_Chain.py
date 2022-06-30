from typing import List


class Solution:
    """
        You are given an array of words where each word consists of lowercase English letters.

        wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

        For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
        A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

        Return the length of the longest possible word chain with words chosen from the given list of words.

        Example 1:

        Input: words = ["a","b","ba","bca","bda","bdca"]
        Output: 4
        Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
        Example 2:

        Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
        Output: 5
        Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
        Example 3:

        Input: words = ["abcd","dbqca"]
        Output: 1
        Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
        ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

        Constraints:

        1 <= words.length <= 1000
        1 <= words[i].length <= 16
        words[i] only consists of lowercase English letters.
    """
    def longestStrChain1(self, words: List[str]) -> int:
        if not words:
            return 0

        def checkPredecessor(word1: str, word2: str):
            if len(word1) + 1 != len(word2):
                return False

            for i in range(len(word2)):
                if word1 == word2[:i] + word2[i + 1:]:
                    return True

            return False
        n = len(words)
        dp = [1] * n
        words.sort(key=lambda x: len(x))
        for i in range(n):
            for j in range(i):
                if checkPredecessor(words[j], words[i]):
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def longestStrChain(self, words: List[str]) -> int:
        wordDict = {}
        words.sort(key=lambda x: len(x))
        for word in words:
            wordDict[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in wordDict:
                    wordDict[word] = max(1 + wordDict[predecessor], wordDict[word])
        return max(wordDict.values())