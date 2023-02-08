from typing import List


class Solution:
    """
        Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

        A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

        Example 1:

        Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
        Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
        Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
        "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
        "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
        Example 2:

        Input: words = ["cat","dog","catdog"]
        Output: ["catdog"]
    """
    def findAllConcatenatedWordsInADict_not_pass(self, words: List[str]) -> List[str]:
        # def check(trie, word, idx):
        #     if idx == len(word):
        #         return True
        #
        #     t = trie
        #     ret = False
        #     for i in range(idx, len(word)):
        #         if word[i] in t:
        #             t = t[word[i]]
        #         else:
        #             return False
        #
        #         if '#' in t:
        #             ret |= check(trie, word, idx + 1)
        #         if ret:
        #             return ret
        #     return ret
        def check(word, idx, trie, cnt):
            n = len(word)
            t = trie
            for i in range(idx, n):
                if word[i] in t:
                    t = t[word[i]]
                if '#' in t:
                    if i == n - 1:
                        return cnt >= 1
                    elif check(word, idx + 1, trie, cnt + 1):
                        return True
            return False

        def insert(word, trie):
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['#'] = {}

        # words.sort(key=lambda x: len(x))
        trie = {}
        ans = []
        for word in words:
            insert(word, trie)
        for word in words:
            if check(word, 0, trie, 0):
                ans.append(word)
            # insert(word, trie)
        return ans

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        ans = []

        def dfs(word):
            if word == "":
                return True

            for i in range(len(word)):
                if word[:i + 1] in word_set and dfs(word[i + 1:]):
                    return True
            return False

        for word in words:
            word_set.discard(word)
            if dfs(word):
                ans.append(word)
            word_set.add(word)
        return ans
