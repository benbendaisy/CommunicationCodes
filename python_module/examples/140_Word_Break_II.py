from typing import List


class Solution:
    """
    Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.

    Example 1:

    Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    Output: ["cats and dog","cat sand dog"]
    Example 2:

    Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
    Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
    Explanation: Note that you are allowed to reuse a dictionary word.
    Example 3:

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: []
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        word_dict = set(wordDict)
        @lru_cache(None)
        def word_break(str1):
            if str1 == "":
                return ""
            res = []
            for i in range(1, len(str1) + 1):
                if str1[:i] in word_dict:
                    ret = word_break(str1[i:])
                    for el in ret:
                        res.append(str1[:i] + " " + el)
                    if ret == "":
                        res.append(str1[:i])
            return res
        return word_break(s)