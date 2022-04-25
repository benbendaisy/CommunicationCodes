import functools


class Solution:
    def __init__(self):
        self.maxLength = 0

    def longestPalindromeSubseq(self, s: str) -> int:
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

if __name__ == "__main__":
    s = "bbbab"
    solution = Solution()
    ret = solution.longestPalindromeSubseq(s)
    print(ret)