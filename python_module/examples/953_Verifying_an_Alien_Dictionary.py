from typing import List


class Solution:
    """
        In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

        Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

        Example 1:

        Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
        Output: true
        Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
        Example 2:

        Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
        Output: false
        Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
        Example 3:

        Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
        Output: false
        Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
    """
    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        n = len(order)
        char_dict = {}
        for i,ch in enumerate(order):
            char_dict[ch] = i
        
        def compare_two_words(word1: str, word2: str):
            l, r = 0, 0
            n1, n2 = len(word1), len(word2)
            while l < n1 and r < n2 and word1[l] == word2[r]:
                l, r = l + 1, r + 1
            if l == n1 and r == n2:
                return 0
            elif l == n1 and r < n2:
                return -1
            elif l < n1 and r == n2:
                return 1
            return -1 if char_dict[word1[l]] < char_dict[word2[r]] else 1
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if compare_two_words(words[i], words[j]) > 0:
                    return False
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(order)
        char_dict = {}
        for i,ch in enumerate(order):
            char_dict[ch] = i
        n = len(words)
        for i in range(n - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if char_dict[words[i][j]] > char_dict[words[i + 1][j]]:
                        return False
                    break
        return True