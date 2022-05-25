import collections
from collections import defaultdict, Counter
from typing import List

class Solution:
    """
        There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

        You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

        Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

        A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

        Example 1:

        Input: words = ["wrt","wrf","er","ett","rftt"]
        Output: "wertf"
        Example 2:

        Input: words = ["z","x"]
        Output: "zx"
        Example 3:

        Input: words = ["z","x","z"]
        Output: ""
        Explanation: The order is invalid, so return "".

        Constraints:

        1 <= words.length <= 100
        1 <= words[i].length <= 100
        words[i] consists of only lowercase English letters.
    """
    def alienOrder1(self, words: List[str]) -> str:
        adjList = defaultdict(set)
        inDegree = Counter({ch: 0 for word in words for ch in word})

        for word1, word2 in zip(words, words[1:]):
            for x, y in zip(word1, word2):
                if x != y:
                    if y not in adjList[x]:
                        adjList[x].add(y)
                        inDegree[y] += 1
                    break
            else:
                if len(word2) < len(word1): return ""

        res = []
        queue = collections.deque([ch for ch in inDegree if inDegree[ch] == 0])
        while queue:
            ch = queue.popleft()
            res.append(ch)
            for nch in adjList[ch]:
                inDegree[nch] -= 1
                if inDegree[nch] == 0:
                    queue.append(nch)

        if len(res) < len(adjList): return ""
        return "".join(res)


    def alienOrder(self, words: List[str]) -> str:
        graph = {ch: [] for word in words for ch in word}

        for word1, word2 in zip(words, words[1:]):
            for x, y in zip(word1, word2):
                if x != y:
                    graph[y].append(x)
                    break
            else:
                if len(word2) < len(word1): return ""

        visited = {}
        res = []
        def dfs(ch):
            if ch in visited:
                return visited[ch]

            visited[ch] = False
            for nch in graph[ch]:
                result = dfs(nch)
                if not result:
                    return False

            visited[ch] = True
            res.append(ch)
            return True

        if not all(dfs(ch) for ch in graph): return ""
        return "".join(res)

