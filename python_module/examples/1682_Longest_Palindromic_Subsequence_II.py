from functools import lru_cache


class Solution:
    def __init__(self):
        self.maxCnt = 0

    @lru_cache(None)
    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) % 2 != 0:
            return False

        if s == s[::-1]:
            if len(s) == 2:
                return True
            else:
                mid = len(s) // 2
                if s[mid] != s[mid + 1]:
                    return True

        return False

    def longestPalindromeSubseq1(self, s: str) -> int:

        # def longestPalSub(str1: str):
        #     if self.validPalindrome(str1):
        #         if len(str1) > self.maxCnt:
        #             self.maxCnt = len(str1)
        #         return
        #
        #     for i in range(0, len(str1)):
        #         subStr = str1[:i] + str1[i + 1:]
        #         longestPalSub(subStr)
        # def longestPalSub(left: int, right: int, prev: str):
        #     if left >= right:
        #         return 0
        #     elif (left, right, prev) in memo:
        #         return memo[(left, right, prev)]
        #
        #     if s[left] == s[right] and s[left] != prev:
        #         memo[(left, right, prev)] = 2 + longestPalSub(left + 1, right - 1, s[left])
        #         return memo[(left, right, prev)]
        #
        #     memo[(left, right, prev)] = max(longestPalSub(left + 1, right, prev), longestPalSub(left, right - 1, prev))
        #     return memo[(left, right, prev)]

        @lru_cache(None)
        def longestPalSub(left: int, right: int, prev: str):
            if left >= right:
                return 0

            if s[left] == s[right] and s[left] != prev:
                return 2 + longestPalSub(left + 1, right - 1, s[left])

            return max(longestPalSub(left + 1, right, prev), longestPalSub(left, right - 1, prev))

        return longestPalSub(0, len(s) - 1, "$")

    def longestPalindromeSubseq2(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j] and s[j] != s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[n][n]

    def longestPalindromeSubseq(self, s: str) -> int:
        maxLength = 0
        def palindromicSubs(idx: int, curStr: str):
            if idx == len(s):
                if len(curStr) % 2 == 0 and curStr == curStr[::-1]:
                    idx1, idx2 = len(curStr) // 2, len(curStr) // 2 + 1
                    if curStr[idx1] != curStr[idx2] and self.maxCnt < len(curStr):
                        self.maxCnt = len(curStr)
                return
            elif len(curStr) % 2 == 0 and curStr == curStr[::-1]:
                if len(curStr) == 2:
                    self.maxCnt = max(self.maxCnt, len(curStr))
                else:
                    idx1, idx2 = len(curStr) // 2, len(curStr) // 2 + 1
                    if curStr[idx1] != curStr[idx2] and self.maxCnt < len(curStr):
                        self.maxCnt = len(curStr)
            i = idx + 1
            while i < len(s):
                curStr += s[i]
                palindromicSubs(i, curStr)
                curStr = curStr[:-1]
                i += 1

        palindromicSubs(-1, "")
        return self.maxCnt


if __name__ == "__main__":
    s = "bbabab"
    solution = Solution()
    ret = solution.longestPalindromeSubseq(s)
    print(ret)