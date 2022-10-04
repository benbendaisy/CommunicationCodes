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
    def maxProfit1(self, k: int, prices: List[int]) -> int:
        # validate input
        # solve special cases
        if not prices or k < 1:
            return 0
        n = len(prices)
        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n)]

        # optimize the result that can be skipped
        if 2 * k > n:
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

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        """
        Use the idea of "reinvesting", we can "carry-over" a
        previous transaction into the next transaction in order
        to calculate a total profit.

        For example, given [3,2,6,5,7,0,3]

        If k = 1, then we would keep track of the lowest price and
        max profit for each day.

            3, min_price [3], max_profit [0]
            2, min_price [2], max_profit [0]
            6, min_price [2], max_profit [4]
            5, min_price [2], max_profit [4]
            7, min_price [2], max_profit [5]
            0, min_price [0], max_profit [5]
            3, min_price [0], max_profit [5]

        If k = 2, we want to understand how much money we could make
        if we "reinvest" profit from k = 1. This means we could only
        initiate a k=2 transaction IFF k=1 (on a previous day) has a
        non-zero max_profit.

            3, min_price [3, 3], max_profit [0, 0]
            2, min_price [2, 2], max_profit [0, 0]
            6, min_price [2, 2], max_profit [4, 4]
            5, min_price [2, 1], max_profit [4, 4]  <- Reinvest profit
            7, min_price [2, 1], max_profit [5, 6]
            0, min_price [0, -5], max_profit [5, 6]
            3, min_price [0, -5], max_profit [5, 8] <- Max profit with 2 transactions

        Notice that the new min_price is $1 when price is $5. Similarly, the new min_price
        is -$5 when price is $0. Why?

        To understand, imagine if we bought at $2 and sold at $6. Then bought at $5
        and sold at $7. That is two transactions with a total profit of
        $4 + $2 = $6.

        Alternative, we can also think of it as (-$2)(+$6)(-$5)(+$7). This means when
        the stock is at $5, we will use our profit to bring its effective price
        down to $1 (i.e. (-$2)(+$6)(-$5)). When we sell at $7, we capture a TOTAL
        profit of $6. Our tabulation is cumulative.


        If k = 3, we do the same thing:

            3, min_price [3, 3, 3], max_profit [0, 0, 0]
            2, min_price [2, 2, 2], max_profit [0, 0, 0]
            6, min_price [2, 2, 2], max_profit [4, 4, 4]
            5, min_price [2, 1, 1], max_profit [4, 4, 4]
            7, min_price [2, 1, 1], max_profit [5, 6, 6]
            0, min_price [0, -5, -6], max_profit [5, 6, 6]
            3, min_price [0, -5, -6], max_profit [5, 8, 9]
        """
        min_price = [float("inf")] * (k + 1)
        max_profit = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                min_price[i] = min(min_price[i], price - max_profit[i - 1])
                max_profit[i] = max(max_profit[i], price - min_price[i])

        return max_profit[k]

    def maxProfit3(self, k: int, prices: List[int]) -> int:
        buy = [-math.inf] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)
        return sell[-1]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        # no transaction, no profit
        if k < 1:
            return 0

        # dp[k][0] = min cost you need to spend at most k transactions
        # dp[k][1] = max profit you can achieve at most k transactions
        dp = [[1000, 0] for _ in range(k + 1)]
        for price in prices:
            for i in range(1, k + 1):
                # price - dp[i - 1][1] is how much you need to spend
                # i.e use the profit you earned from previous transaction to buy the stock
                # we want to minimize it
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                # price - dp[i][0] is how much you can achieve from previous min cost
                # we want to maximize it
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        # return max profit at most k transactions
        # or you can write `return dp[-1][1]
        return dp[k][1]

if __name__ == "__main__":
    prices = [2,4,1]
    k = 2
    solution = Solution()
    ret = solution.maxProfit(k, prices)
    print(ret)