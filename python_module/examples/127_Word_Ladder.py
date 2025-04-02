class Solution:
    """
    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
    Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

    Example 1:

    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    Example 2:

    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: 0
    Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
    """
    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time limit exceeded for large test cases
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        visited = set()
        @cache
        def helper(word: str, cnt: int):
            if word == endWord:
                return cnt
            visited.add(word)
            min_step = float('inf')
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if word[i] != ch:
                        new_word = word[:i] + ch + word[i + 1:]
                        if new_word in word_set and new_word not in visited:
                            min_step = min(min_step, helper(new_word, cnt + 1))
            visited.remove(word)
            return min_step
        res = helper(beginWord, 1)
        return 0 if res == float('inf') else res
    
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        visited = set([beginWord])
        que = deque([(beginWord, 1)])
        while que:
            word, cnt = que.popleft()
            if word == endWord:
                return cnt
            visited.add(word)
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in word_set and new_word not in visited:
                        que.append((new_word, cnt + 1))
            
        return 0
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        que = deque([(beginWord, 1)])
        while que:
            word, cnt = que.popleft()
            if word == endWord:
                return cnt
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in word_set:
                        que.append((new_word, cnt + 1))
                        word_set.remove(new_word)
            
        return 0