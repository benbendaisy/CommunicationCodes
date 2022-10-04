from typing import List


class Solution:
    """
        Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

        Example 1:

        Input: words = ["abcd","dcba","lls","s","sssll"]
        Output: [[0,1],[1,0],[3,2],[2,4]]
        Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
        Example 2:

        Input: words = ["bat","tab","cat"]
        Output: [[0,1],[1,0]]
        Explanation: The palindromes are ["battab","tabbat"]
        Example 3:

        Input: words = ["a",""]
        Output: [[0,1],[1,0]]


        Constraints:

        1 <= words.length <= 5000
        0 <= words[i].length <= 300
        words[i] consists of lower-case English letters.
    """
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:
        arr = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue

                concatedStr = word1 + word2
                if concatedStr == concatedStr[::-1]:
                    arr.append([i, j])
        return arr

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])

            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])

            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j - 1::-1]:
                    res.append([backward[word[j:]], i])

                if word[:j] in backward and word[j:] == word[:j - 1:-1]:
                    res.append([i, backward[word[:j]]])

        return res