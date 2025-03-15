class Solution:
    """
    Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

    You may assume that no string in words is a substring of another string in words.

    Example 1:

    Input: words = ["alex","loves","leetcode"]
    Output: "alexlovesleetcode"
    Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
    Example 2:

    Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    Output: "gctaagttcatgcatc"
    """
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlap = [[''] * n for _ in range(n)]

        def getOverlap(a, b):
            l, i = 0, 1
            while i <= min(len(a), len(b)):
                if a[len(a)-i:] == b[:i]:
                    l = i
                i += 1
            return b[l:]

        for i in range(n):
            for j in range(n):
                if i != j: overlap[i][j] = getOverlap(words[i], words[j])

        @cache
        def helper(prev, mask):
            if mask == ((1 << n) - 1): return ''
            ans = '*' * 1000000
            for i in range(n):
                if mask & (1 << i): 
                    continue
                word = overlap[prev][i] if prev != -1 else words[i]
                ans = min(ans, word + helper(i, mask | (1 << i)), key=len)
            return ans

        return helper(-1, 0)