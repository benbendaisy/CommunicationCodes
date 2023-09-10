class Solution:
    def minimumDeleteSum1(self, s1: str, s2: str) -> int:
        prev_row = [0] * (len(s2) + 1)
        for j in range(1, len(s2) + 1):
            prev_row[j] = prev_row[j - 1] + ord(s2[j - 1])
        for i in range(1, len(s1) + 1):
            curr_row = [prev_row[0] + ord(s1[i - 1])]
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr_row.append(prev_row[j - 1])
                else:
                    curr_row.append(min(prev_row[j] + ord(s1[i - 1]), curr_row[j - 1] + ord(s2[j - 1])))
            prev_row = curr_row
        return prev_row[-1]
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def lcs(s, p):
            m, n = len(s), len(p)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    if s[i] == p[j]:
                        dp[i + 1][j + 1] = dp[i][j] + ord(s[i])
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
            return dp[-1][-1]
        common_cs = lcs(s1, s2)
        total, res = 0, 0
        for c in s1:
            total += ord(c)
        for c in s2:
            total += ord(c)
        res = total - common_cs * 2
        return res

