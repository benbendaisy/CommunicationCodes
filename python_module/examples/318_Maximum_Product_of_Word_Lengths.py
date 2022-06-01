from collections import Counter
from typing import List


class Solution:
    """
        Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

        Example 1:

        Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
        Output: 16
        Explanation: The two words can be "abcw", "xtfn".
        Example 2:

        Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
        Output: 4
        Explanation: The two words can be "ab", "cd".
        Example 3:

        Input: words = ["a","aa","aaa","aaaa"]
        Output: 0
        Explanation: No such pair of words.

        Constraints:

        2 <= words.length <= 1000
        1 <= words[i].length <= 1000
        words[i] consists only of lowercase English letters.
    """
    def maxProduct(self, words: List[str]) -> int:
        def checkOverlap(str1: str, str2: str):
            for ch in str1:
                if ch in str2:
                    return True
            return False

        maxProduct = 0
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not checkOverlap(words[i], words[j]):
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))

        return maxProduct
