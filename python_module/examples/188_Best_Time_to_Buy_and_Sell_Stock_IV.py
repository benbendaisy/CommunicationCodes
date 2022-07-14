import math
from typing import List


class Solution:
    """
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

        Find the maximum profit you can achieve. You may complete at most k transactions.
        
        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
        
        Example 1:
        
        Input: k = 2, prices = [2,4,1]
        Output: 2
        Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
        Example 2:
        
        Input: k = 2, prices = [3,2,6,5,0,3]
        Output: 7
        Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

        Constraints:
        
        0 <= k <= 100
        0 <= prices.length <= 1000
        0 <= prices[i] <= 1000
    """
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # validate input
        if not prices or k < 1:
            return 0
        n = len(prices)
        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n)]

        # optimize the result that can be skipped
        if 2*k > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        # set starting value
        dp[0][0][0] = 0
        # buy first stock
        dp[0][1][1] = -prices[0]
        for i in range(1, n):
            for j in range(k + 1):
                # transition equation
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                if j > 0:
                    # buy stock
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i-1][j-1][0] - prices[i])
        return max(dp[n - 1][j][0] for j in range(k + 1))