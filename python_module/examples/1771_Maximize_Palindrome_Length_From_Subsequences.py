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

    def longestPalindrome2(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return 0
        length1 = len(word1)
        length2 = len(word2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        word3 = word2[::-1]
        for i in range(length1 + 1):
            for j in range(length2 + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                if word1[i - 1] == word3[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[length1][length2]

    def longestPalindrome3(self, word1: str, word2: str) -> int:
        def longestCommonSubsequence(str1: str, str2: str, idx1: int, idx2: int):
            if idx1 >= len(str1) or idx2 >= len(str2):
                return 0

            if str1[idx1] == str2[idx2]:
                return 1 + longestCommonSubsequence(str1, str2, idx1 + 1, idx2 + 1)
            else:
                return max(longestCommonSubsequence(str1, str2, idx1 + 1, idx2), longestCommonSubsequence(str1, str2, idx1, idx2 + 1))
        return longestCommonSubsequence(word1, word2[::-1], 0, 0)

    def longestPalindrome3(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return 0
        l1, l2 = len(word1), len(word2)
        word = word1 + word2
        dp = [[0] * (l1 + l2) for _ in range(l1 + l2)]
        maxLength = 0
        for j in range(l1 + l2):
            for i in range(j, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = j - i + 1 if j - i < 2 else dp[i + 1][j - 1] + 2
                    if i < l1 and j >= l1: maxLength = max(maxLength, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return maxLength

if __name__ == "__main__":
    word1, word2 = "cacb", "cbba"
    solution = Solution()
    ret = solution.longestPalindrome3(word1, word2)
    print(ret)