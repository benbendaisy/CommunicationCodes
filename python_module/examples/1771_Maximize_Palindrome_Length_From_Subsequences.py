class Solution:
    def __init__(self):
        self.maxCount = 0

    def concatPalindrome(self, word1: str, word2: str, idx1: int, idx2: int):
        length1 = len(word1)
        length2 = len(word2)
        if idx1 == length1 or idx2 == length2:
            return
        for i in range(idx1 + 1, length1 + 1):
            for j in range(idx2 + 1, length2 + 1):
                s = word1[idx1:i] + word2[idx2:j]
                if s == s[::-1] and len(s) > self.maxCount:
                    self.maxCount = len(s)
        if word1[idx1] == word2[idx2]:
            self.concatPalindrome(word1, word2, idx1 + 1, idx2 + 1)
        else:
            self.concatPalindrome(word1, word2, idx1 + 1, idx2)
            self.concatPalindrome(word1, word2, idx1, idx2 + 1)

    def longestPalindrome1(self, word1: str, word2: str) -> int:
        self.concatPalindrome(word1, word2, 0, 0)
        return self.maxCount

    def longestPalindrome(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)
        dp = [[0 for _ in range(length1 + 1)] for _ in range(length2 + 1)]
        ans = 0
        for i in range(1, length1):
            for j in range(length2 - 1, 0, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = max(dp[i][j], 2 + dp[i - 1][j + 1])
                    if ans < dp[i][j]:
                        ans = dp[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j + 1])
        return ans

if __name__ == "__main__":
    word1, word2 = "cacb", "cbba"
    solution = Solution()
    ret = solution.longestPalindrome(word1, word2)
    print(ret)