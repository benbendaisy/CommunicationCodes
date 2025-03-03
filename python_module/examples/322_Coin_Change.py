import math
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    """
        You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

        You may assume that you have an infinite number of each kind of coin.

        Example 1:

        Input: coins = [1,2,5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1
        Example 2:

        Input: coins = [2], amount = 3
        Output: -1
        Example 3:

        Input: coins = [1], amount = 0
        Output: 0

        Constraints:

        1 <= coins.length <= 12
        1 <= coins[i] <= 231 - 1
        0 <= amount <= 104
    """
    def coinChange1(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def coinChanges(amt: int) -> int:
            if amt == 0:
                return 0
            elif amt < 0:
                return -1

            locCnt = math.inf
            for coin in coins:
                subCnt = coinChanges(amt - coin)
                if subCnt >= 0:
                    locCnt = min(locCnt, subCnt + 1)
            return -1 if locCnt == math.inf else locCnt

        return coinChanges(amount)

    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != math.inf else -1
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        
        @cache
        def helper(cur_sum: int):
            if cur_sum == amount:
                return 0
            
            min_num = float('inf')
            for coin in coins:
                t = cur_sum + coin
                if t <= amount:
                    min_num = min(min_num, 1 + helper(t))
            return min_num
        res = helper(0)
        return -1 if res == float('inf') else res

if __name__ == "__main__":
    coins = [474,83,404,3]
    amount = 264
    solution = Solution()
    ret = solution.coinChange(coins, amount)
    print(ret)