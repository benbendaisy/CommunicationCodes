from typing import List


class Solution:
    """
        You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

        Return the maximum possible length of s.

        A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

        Example 1:

        Input: arr = ["un","iq","ue"]
        Output: 4
        Explanation: All the valid concatenations are:
        - ""
        - "un"
        - "iq"
        - "ue"
        - "uniq" ("un" + "iq")
        - "ique" ("iq" + "ue")
        Maximum length is 4.
        Example 2:

        Input: arr = ["cha","r","act","ers"]
        Output: 6
        Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
        Example 3:

        Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
        Output: 26
        Explanation: The only string in arr has all 26 characters.
    """
    def maxLength1(self, arr: List[str]) -> int:
        if not arr:
            return 0

        res = [""]
        maxLength = 0
        for word in arr:
            for i in range(len(res)):
                concatedString = res[i] + word
                if len(concatedString) != len(set(concatedString)):
                    continue
                maxLength = max(maxLength, len(concatedString))
                res.append(concatedString)
        return maxLength
    
    def maxLength(self, arr: List[str]) -> int:
        res = [""]
        best = 0
        for word in arr:
            for i in range(len(res)):
                new_res = res[i] + word
                if len(new_res) != len(set(new_res)):
                    continue
                res.append(new_res)
                best = max(best, len(new_res))
        return best
