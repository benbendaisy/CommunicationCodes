import functools


class Solution:
    def __init__(self):
        self.maxLength = 0

    def longestPalindromeSubseq0(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        s2 = s[::-1]
        for i in range(1, length + 1):
            for j in range(1, length + 1):
                if s[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[length][length]



    def longestPalindromeSubseq1(self, s: str) -> int:
        @functools.lru_cache(None)
        def longestPalindromeSub(str1: str):
            length = len(str1)
            if not str1:
                return 0
            elif str1 == str1[::-1]:
                self.maxLength = max(self.maxLength, length)
                return length

            for i in range(0, length):
                str2 = str1[:i] + str1[i + 1:]
                longestPalindromeSub(str2)

        longestPalindromeSub(s)
        return self.maxLength
    
    def longestPalindromeSubseq2(self, s: str) -> int:
        if not s:
            return 0
        
        @cache
        def helper(path: str) -> int:
            if not path:
                return 0
            
            if path == path[::-1]:
                return len(path)

            max_len = float('-inf')
            n = len(path)
            for i in range(n):
                max_len = max(max_len, helper(path[:i] + path[i + 1:]))
            return max_len
        
        return helper(s)
    
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        @cache
        def helper(left: int, right: int) -> int:
            if left > right:
                return 0
            
            if left == right:
                return 1
            
            if s[left] == s[right]:
                return 2 + helper(left + 1, right - 1)
            
            return max(helper(left + 1, right), helper(left, right - 1))
        
        return helper(0, len(s) - 1)

if __name__ == "__main__":
    s = "bbbab"
    solution = Solution()
    ret = solution.longestPalindromeSubseq(s)
    print(ret)