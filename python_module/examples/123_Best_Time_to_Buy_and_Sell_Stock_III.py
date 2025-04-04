import heapq
from typing import List


class Solution:
    """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        Find the maximum profit you can achieve. You may complete at most two transactions.

        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

        Example 1:

        Input: prices = [3,3,5,0,0,3,1,4]
        Output: 6
        Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
        Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
        Example 2:

        Input: prices = [1,2,3,4,5]
        Output: 4
        Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
        Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
        Example 3:

        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transaction is done, i.e. max profit = 0.

        Constraints:

        1 <= prices.length <= 105
        0 <= prices[i] <= 105
    """
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices or len(prices) < 1:
            return -1
        n = len(prices)
        leftProfit = [0] * n
        rightProfit = [0] * (n + 1)
        leftMin, rightMax = prices[0], prices[-1]
        for i in range(1, n):
            leftProfit[i] = max(leftProfit[i - 1], prices[i] - leftMin)
            leftMin = min(leftMin, prices[i])

        for j in range(n - 1, -1, -1):
            rightProfit[j] = max(rightProfit[j + 1], rightMax - prices[j])
            rightMax = max(rightMax, prices[j])

        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, leftProfit[i] + rightProfit[i + 1])
        return maxProfit
    
    def maxProfit2(self, prices: List[int]) -> int:
        """
        tle
        """
        def max_profits(arr: List[int]):
            if len(arr) < 2:
                return 0
            min_price, max_profit = float('inf'), float('-inf')
            for price in arr:
                min_price = min(min_price, price)
                max_profit = max(max_profit, price - min_price)
            return max_profit
        
        max_profit = float('-inf')
        for i in range(len(prices)):
            max_split = max_profits(prices[:i + 1]) + max_profits(prices[i + 1:])
            max_profit = max(max_profit, max_split)
        return max_profit

    def maxProfit3(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        
        # Step 1: Compute max profit from left (0 to i)
        left_profit = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)

        # Step 2: Compute max profit from right (i to n-1)
        right_profit = [0] * n
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profit[i] = max(right_profit[i + 1], max_price - prices[i])

        # Step 3: Find the best split
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profit[i] + (right_profit[i + 1] if i + 1 < n else 0))

        return max_profit
    
    def maxProfit4(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        left_max_profit = [0] * n
        right_max_profit = [0] * n

        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_max_profit[i] = max(left_max_profit[i - 1], prices[i] - min_price)

        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_max_profit[i] = max(right_max_profit[i + 1], max_price - prices[i])

        max_profit = float('-inf')
        for i in range(n):
            profit = left_max_profit[i] + (right_max_profit[i + 1] if i + 1 < n else 0)
            max_profit = max(max_profit, profit)
        return max_profit
    
    def maxProfit5(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        
        @cache
        def helper(idx: int, p: int, holding: bool):
            if idx == n or p == 0:
                return 0
            
            max_profit = helper(idx + 1, p, holding)

            if holding:
                max_profit = max(max_profit, prices[idx] + helper(idx + 1, p - 1, False))
            else:
                max_profit = max(max_profit, -prices[idx] + helper(idx + 1, p, True))
            return max_profit
        
        return helper(0, 2, False)
    
    def maxProfit6(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        @cache
        def helper(idx: int, ops: int, holding: bool):
            if idx == n or ops == 2:
                return 0

            # sip current
            max_profit = helper(idx + 1, ops, holding)
            if holding:
                # sell stock
                max_profit = max(max_profit, helper(idx + 1, ops + 1, False) + prices[idx])
            else:
                # buy stock
                max_profit = max(max_profit, helper(idx + 1, ops, True) - prices[idx])
            return max_profit
        return helper(0, 0, False)
    
    def maxProfit6(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        max_left_profit = [0] * n
        max_right_profit = [0] * n
        
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            max_left_profit[i] = max(max_left_profit[i - 1], prices[i] - min_price)
        
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            max_right_profit[i] = max(max_right_profit[i + 1], max_price - prices[i])
        max_profits = 0
        for i in range(n):
            profit = max_left_profit[i] + (max_right_profit[i + 1] if i + 1 < n else 0)
            max_profits = max(max_profits, profit)
        return max_profits
