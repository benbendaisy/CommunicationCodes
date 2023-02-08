from typing import List


class Solution:
    """
        Given a string s, partition s such that every
        substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

        Example 1:

        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]
        Example 2:

        Input: s = "a"
        Output: [["a"]]
    """
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        if n == 0:
            return [[]]
        for i in range(1, n + 1):
            if s[:i] != s[:i][::-1]:
                continue
            cur = self.partition(s[i:])
            for j in range(len(cur)):
                ans.append([s[:i]] + cur[j])
        return ans