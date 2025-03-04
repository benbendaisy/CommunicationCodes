from functools import lru_cache


class Solution:
    """
        You have n dice and each die has k faces numbered from 1 to k.

        Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

        Example 1:

        Input: n = 1, k = 6, target = 3
        Output: 1
        Explanation: You throw one die with 6 faces.
        There is only one way to get a sum of 3.
        Example 2:

        Input: n = 2, k = 6, target = 7
        Output: 6
        Explanation: You throw two dice, each with 6 faces.
        There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
        Example 3:

        Input: n = 30, k = 30, target = 500
        Output: 222616187
        Explanation: The answer must be returned modulo 109 + 7.

        Constraints:

        1 <= n, k <= 30
        1 <= target <= 1000
    """
    def numRollsToTarget1(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def waysToTarget(idx, currSum):
            if idx == n:
                return 1 if currSum == target else 0

            ways = 0
            for i in range(1, min(k, target - currSum) + 1):
                ways = (ways + waysToTarget(idx + 1, currSum + i)) % mod
            return ways

        return waysToTarget(0, 0)

    def numRollsToTarget2(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[n][target] = 1
        for idx in range(n - 1, -1, -1):
            for curSum in range(target + 1):
                ways = 0
                for i in range(1, min(k, target - curSum) + 1):
                    ways = (ways + dp[idx + 1][curSum + i]) % mod
                dp[idx][curSum] = ways
        return dp[0][0]

    def numRollsToTarget3(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for idx in range(1, n + 1):
            for currSum in range(target + 1):
                ways = 0
                for i in range(1, min(currSum, k) + 1):
                    ways = (ways + dp[idx - 1][currSum - i]) % mod
                dp[idx][currSum] = ways
        return dp[n][target]
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def helper(idx: int, remaining: int) -> int:
            if remaining == 0:
                return idx == n
            
            if idx == n:
                return 0
            
            ways = 0
            for i in range(1, k + 1):
                if remaining - i >= 0:
                    ways += helper(idx + 1, remaining - i)
            return ways
        
        return helper(0, target) % mod

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    solution = Solution()
    ret = solution.numRollsToTarget(1, 6, 3)
    print(ret)
