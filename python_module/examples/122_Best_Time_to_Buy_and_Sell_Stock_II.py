import math
from typing import List


class Solution:
    """
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

        On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

        Find and return the maximum profit you can achieve.

        Example 1:

        Input: prices = [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
        Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        Total profit is 4 + 3 = 7.
        Example 2:

        Input: prices = [1,2,3,4,5]
        Output: 4
        Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
        Total profit is 4.
        Example 3:

        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

        Constraints:

        1 <= prices.length <= 3 * 104
        0 <= prices[i] <= 104
    """
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices or len(prices) < 1:
            return -1
        curMin = prices[0]
        cnt = 0
        for i in range(1, len(prices)):
            if curMin < prices[i]:
                cnt += prices[i] - curMin
                curMin = prices[i]
            else:
                curMin = prices[i]
        return cnt
    
    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cur_min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if cur_min < prices[i]:
                profit += prices[i] - cur_min
            cur_min = prices[i]
        return profit
    
    def maxProfit3(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        profit = 0
        for i in range(1, n):
            delta = prices[i] - prices[i - 1]
            if delta > 0:
                profit += delta
        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit, n = 0, len(prices)
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                max_profit += diff
        return max_profit