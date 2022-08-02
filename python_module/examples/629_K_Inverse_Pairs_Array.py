from functools import lru_cache


class Solution:
    """
        For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

        Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

        Example 1:

        Input: n = 3, k = 0
        Output: 1
        Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
        Example 2:

        Input: n = 3, k = 1
        Output: 2
        Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

        Constraints:

        1 <= n <= 1000
        0 <= k <= 1000
    """
    @lru_cache(None)
    def kInversePairs1(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        elif k == 0:
            return 1

        inv = 0
        for i in range(min(k, n - 1)):
            inv = (inv + self.kInversePairs(n - 1, k - i))
        return inv

    def kInversePairs2(self, n: int, k: int) -> int:
        dp = [[0] * k for _ in range(n)]
        for i in range(n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    for p in range(min(j, i - 1) + 1):
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - p]) % 1000000007
        return dp[n][k]