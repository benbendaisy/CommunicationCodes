from collections import defaultdict


class Solution:
    """
        Two strings are considered close if you can attain one from the other using the following operations:

        Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
        Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
        You can use the operations on either string as many times as necessary.

        Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

        Example 1:

        Input: word1 = "abc", word2 = "bca"
        Output: true
        Explanation: You can attain word2 from word1 in 2 operations.
        Apply Operation 1: "abc" -> "acb"
        Apply Operation 1: "acb" -> "bca"
        Example 2:

        Input: word1 = "a", word2 = "aa"
        Output: false
        Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
        Example 3:

        Input: word1 = "cabbba", word2 = "abbccc"
        Output: true
        Explanation: You can attain word2 from word1 in 3 operations.
        Apply Operation 1: "cabbba" -> "caabbb"
        Apply Operation 2: "caabbb" -> "baaccc"
        Apply Operation 2: "baaccc" -> "abbccc"
    """
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_map = defaultdict(int)
        word2_map = defaultdict(int)
        for ch in word1:
            word1_map[ch] += 1
        for ch in word2:
            word2_map[ch] += 1
        if word1_map.keys() != word2_map.keys():
            return False
        word1_frequency_list = word1_map.values()
        word2_frequency_list = word2_map.values()
        word1_frequency_list = sorted(word1_frequency_list)
        word2_frequency_list = sorted(word2_frequency_list)
        return word1_frequency_list == word2_frequency_list
