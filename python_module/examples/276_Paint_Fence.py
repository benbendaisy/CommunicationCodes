from functools import lru_cache
from typing import List


class Solution:
    """
        You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

        Every post must be painted exactly one color.
        There cannot be three or more consecutive posts with the same color.
        Given the two integers n and k, return the number of ways you can paint the fence.

        Example 1:

        Input: n = 3, k = 2
        Output: 6
        Explanation: All the possibilities are shown.
        Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
        Example 2:

        Input: n = 1, k = 1
        Output: 1
        Example 3:

        Input: n = 7, k = 2
        Output: 42

        Constraints:

        1 <= n <= 50
        1 <= k <= 105
        The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k.
    """
    def numWays1(self, n: int, k: int) -> int:
        def checkConsecutiveThree(arr: List):
            for i in range(len(arr) - 2):
                cnt = 1
                for j in range(i + 1, i + 3):
                    if arr[j] != arr[i]:
                        break
                    cnt += 1
                if cnt == 3:
                    return True
            return False

        def numOfWays(idx: int, arr: List):
            if idx == n:
                if not checkConsecutiveThree(arr):
                    return 1
                else:
                    return 0
            cnt = 0
            for i in range(k):
                cnt += numOfWays(idx + 1, arr + [i])
            return cnt

        return numOfWays(0, [])

    def numWays2(self, n: int, k: int) -> int:
        @lru_cache(None)
        def totalWays(m: int):
            if m == 1:
                return k
            elif m == 2:
                return k * k

            return (k - 1) * (totalWays(m - 1) + totalWays(m - 2))
        return totalWays(n)

    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        elif n == 2:
            return k * k
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        for i in range(3, n + 1):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        return dp[n]
if __name__ == "__main__":
    solution = Solution()
    ret = solution.numWays(2, 46340)
    print(ret)
