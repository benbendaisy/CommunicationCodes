import math
from functools import lru_cache
from typing import List


class Solution:
    """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

        After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

        Example 1:

        Input: prices = [1,2,3,0,2]
        Output: 3
        Explanation: transactions = [buy, sell, cooldown, buy, sell]
        Example 2:

        Input: prices = [1]
        Output: 0

        Constraints:

        1 <= prices.length <= 5000
        0 <= prices[i] <= 1000
    """
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(idx: int, holding: bool, cooldown: bool):
            if idx == n:
                return 0
            doNothing = dp(idx + 1, holding, False)
            doSomething = -math.inf
            if not cooldown:
                if holding: #sell the stock
                    doSomething = max(doSomething, prices[idx] + dp(idx + 1, False, True))
                else: #buy the stock
                    doSomething = max(doSomething, -prices[idx] + dp(idx + 1, True, False))
            return max(doNothing, doSomething)
        return dp(0, False, False)

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (2) for _ in range(2)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for holding in range(2):
                for cooldown in range(2):
                    doNothing = dp[i + 1][holding][0]
                    doSomthing = -math.inf
                    if not cooldown:
                        if holding: #sell stock, holding = 0 and cooldown = 1 means just sell stock
                            doSomthing = max(doSomthing, prices[i] + dp[i + 1][0][1])
                        else: #buy stock, holding = 1 and cooldown = 0 means buy stock
                            doSomthing = max(doSomthing, -prices[i] + dp[i + 1][1][0])
                    dp[i][holding][cooldown] = max(doNothing, doSomthing)
        return dp[0][0][0]