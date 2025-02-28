from typing import List


class Solution:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

    Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Example 1:

    Input: prices = [1,3,2,8,4,9], fee = 2
    Output: 8
    Explanation: The maximum profit can be achieved by:
    - Buying at prices[0] = 1
    - Selling at prices[3] = 8
    - Buying at prices[4] = 4
    - Selling at prices[5] = 9
    The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
    Example 2:

    Input: prices = [1,3,7,5,10,3], fee = 3
    Output: 6
    """
    def maxProfit1(self, prices: List[int], fee: int) -> int:
        profit_cum = float("-inf")
        profit_sum = 0
        for price in prices:
            profit_cum = max(profit_cum, profit_sum - price) # check whether buy or not
            profit_sum = max(profit_sum, profit_cum + price - fee) # check whether sell or not
        return profit_sum
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        n = len(prices)
        @cache
        def helper(idx: int, holding: bool):
            if idx == n:
                return 0
            
            max_profit = helper(idx + 1, holding)
            if holding:
                max_profit = max(max_profit, prices[idx] - fee + helper(idx + 1, False))
            else:
                max_profit = max(max_profit, -prices[idx] + helper(idx + 1, True))
            
            return max_profit
        return helper(0, False)