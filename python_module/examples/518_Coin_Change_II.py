from typing import List


class Solution:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

    Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.

    Example 1:

    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
    Example 2:

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
    Example 3:

    Input: amount = 10, coins = [10]
    Output: 1
    """
    def change1(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for i in range(n):
            coin = coins[i]
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]
    
    def change2(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def make_changes(i, t):
            if t == 0:
                return 1
            if t < 0:
                return 0
            if i >= len(coins):
                return 0
            coin = coins[i]
            # take c1 from coin
            c1 = make_changes(i, t - coin)
            # not take c1
            c2 = make_changes(i + 1, t)
            return c1 + c2
        return make_changes(0, amount)
    
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins:
            return 0
        @cache
        def helper(cur_sum: int) -> int:
            if cur_sum == amount:
                return 1
            
            num_comb = 0
            for coin in coins:
                t = cur_sum + coin
                if t <= amount:
                    num_comb += helper(t)
            return num_comb
        
        return helper(0)
    
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1 # One way to make zero (by choosing nothing)
        if not coins:
            return 0 # No way to make any amount without coins
        n = len(coins)
        @cache # Memoization to avoid redundant calculations
        def helper(idx: int, cur_sum: int) -> int:
            if cur_sum == amount:
                return 1 # Found one valid combination
            if idx == n or cur_sum > amount:
                return 0 # Exceeded target or exhausted coins
            
            # Two choices: 
            # 1. Include the coin `coins[i]` (do not move to the next index)
            # 2. Skip this coin and move to the next index
            return helper(idx + 1, cur_sum) + helper(idx, cur_sum + coins[idx])
        
        return helper(0, 0)
