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
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(order)
        char_dict = {}
        for i in range(n):
            char_dict[order[i]] = i

        def compare_two_words(word1: str, word2: str):
            l = r = 0
            while l < len(word1) and r < len(word2) and word1[l] == word2[r]:
                l, r = l + 1, r + 1
            if l == len(word1) and r == len(word2):
                return 0
            elif l == len(word1) and r < len(word2):
                return -1
            elif l < len(word1) and r == len(word2):
                return 1

            return -1 if char_dict[word1[l]] < char_dict[word2[r]] else 1

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if compare_two_words(words[i], words[j]) > 0:
                    return False
        return True