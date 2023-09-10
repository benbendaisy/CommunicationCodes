from typing import List


class Solution:
    """
        Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

        Note that the same word in the dictionary may be reused multiple times in the segmentation.

        Example 1:

        Input: s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
        Example 2:

        Input: s = "applepenapple", wordDict = ["apple","pen"]
        Output: true
        Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
        Note that you are allowed to reuse a dictionary word.
        Example 3:

        Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        Output: false
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        n = len(s)
        @lru_cache(None)
        def word_break(idx: int):
            if idx >= n or s[idx:] in wordDict:
                return True
            for i in range(idx, n):
                if s[idx:i] in wordDict and word_break(i):
                    return True
            return False
        return word_break(0)
