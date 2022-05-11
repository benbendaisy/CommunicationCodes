class Solution:
    def countVowelStrings1(self, n: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]

        res = []
        def nVowelStrings(m: int, str1: str):
            if m == 0:
                res.append(str1)
                return
            idx = 0
            if len(str1) > 0:
                idx = vowels.index(str1[-1])
            for i in range(idx, len(vowels)):
                nVowelStrings(m - 1, str1 + vowels[i])

        nVowelStrings(n, "")
        return len(res)

    def countVowelStrings2(self, n: int) -> int:
        def coutVowels(m: int, idx: int) -> int:
            if m == 0:
                return 1
            res = 0
            for i in range(idx, 5):
                res += coutVowels(m - 1, i)
            return res

        return coutVowels(n, 0)

    def countVowelStrings3(self, n: int) -> int:
        memo = [[0] * 6 for _ in range(n + 1)]
        def countVowels(m: int, idx: int):
            if m == 0:
                return 1

            if idx == 4:
                return 1

            if memo[m][idx] != 0:
                return memo[m][idx]

            memo[m][idx] = countVowels(m - 1, idx) + countVowels(m, idx + 1)
            return memo[m][idx]

        return countVowels(n, 0)

    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 6 for _ in range(n + 1)]

        for i in range(6):
            dp[1][i] = i

        for i in range(2, n + 1):
            dp[i][1] = 1
            for j in range(2, 6):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n][5]



if __name__ == "__main__":
    n = 44
    solution = Solution()
    ret = solution.countVowelStrings(n)
    print(ret)