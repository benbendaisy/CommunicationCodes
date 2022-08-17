from collections import deque
from typing import List


class Solution:
    """
        A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

        Every adjacent pair of words differs by a single letter.
        Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
        sk == endWord
        Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

        Example 1:

        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
        Explanation: There are 2 shortest transformation sequences:
        "hit" -> "hot" -> "dot" -> "dog" -> "cog"
        "hit" -> "hot" -> "lot" -> "log" -> "cog"
        Example 2:

        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
        Output: []
        Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

        Constraints:

        1 <= beginWord.length <= 5
        endWord.length == beginWord.length
        1 <= wordList.length <= 500
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique
    """
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        # adding beginWord and endWord into the valid word list
        wordList.append(beginWord)
        wordList.append(endWord)
        distance = {}

        # find all valid word distaces to the endWord
        self.bfs(endWord, distance, wordList)

        results = []
        # find all pathes that the included path is from beginWord to endWord
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)

        return results

    def bfs(self, startWord, distance, wordList):
        """
        find the minimal distances that all words to the startWord
        :param startWord: 
        :param distance: 
        :param wordList: 
        :return: 
        """
        distance[startWord] = 0
        queue = deque([startWord])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, wordList):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, wordList):
        """
        get next word that is in wordList
        :param word:
        :param wordList:
        :return:
        """
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in wordList:
                    words.append(next_word)
        return words

    def dfs(self, curt, target, distance, wordList, path, results):
        """
        find all path from beginWord to target included in the path
        :param curt: current word generated from the previous word
        :param target: the target word
        :param distance: the distance dict
        :param wordList: the word lists
        :param path: the word included in the path
        :param results: the final results that include all pathes
        :return: the results that include all possible pathes
        """
        if curt == target:
            results.append(path)
            return

        for word in self.get_next_words(curt, wordList):
            # filter all the pathes that the word to the endWord is not minimal
            if distance[word] != distance[curt] - 1:
                continue
            self.dfs(word, target, distance, wordList, path + [word], results)

