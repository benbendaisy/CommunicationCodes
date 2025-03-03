class Solution:
    """
        Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

        In one step, you can delete exactly one character in either string.

        Example 1:

        Input: word1 = "sea", word2 = "eat"
        Output: 2
        Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
        Example 2:

        Input: word1 = "leetcode", word2 = "etco"
        Output: 4

        Constraints:

        1 <= word1.length, word2.length <= 500
        word1 and word2 consist of only lowercase English letters.
    """
    def minDistance1(self, word1: str, word2: str) -> int:
        def lcs(idx1: int, idx2: int):
            if idx1 == len(word1) or idx2 == len(word2):
                return 0
            elif word1[idx1] == word2[idx2]:
                return 1 + lcs(idx1 + 1, idx2 + 1)
            else:
                return max(lcs(idx1, idx2 + 1), lcs(idx1 + 1, idx2))

        return len(word1) + len(word2) - 2 * lcs(0, 0)

    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return m + n - 2 * dp[m][n]
    
    def minDistance3(self, word1: str, word2: str) -> int:
        """
        Idea: find the longest common subsequence between word1 and word2 and 
        delete the rest of the characters in word1 and word2
        """
        if not word1 or not word2:
            return -1
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return m + n - 2 * dp[m][n]
    
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return -1
        m, n = len(word1), len(word2)
        @cache
        def helper(idx1: int, idx2: int) -> int:
            if idx1 == m:
                return n - idx2
            
            if idx2 == n:
                return m - idx1
            
            if word1[idx1] == word2[idx2]:
                return helper(idx1 + 1, idx2 + 1)
            
            return min(helper(idx1 + 1, idx2), helper(idx1, idx2 + 1)) + 1
        
        return helper(0, 0)