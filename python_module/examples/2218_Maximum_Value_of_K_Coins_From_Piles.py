from functools import lru_cache
from typing import List


class Solution:
    """
        There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

        In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

        Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

        Example 1:

        Input: piles = [[1,100,3],[7,8,9]], k = 2
        Output: 101
        Explanation:
        The above diagram shows the different ways we can choose k coins.
        The maximum total we can obtain is 101.
        Example 2:

        Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
        Output: 706
        Explanation:
        The maximum total can be obtained if we choose all coins from the last pile.
    """
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        @lru_cache(None)
        def func(i, k):
            if k == 0 or i == len(piles):
                return 0
            res, cur = func(i + 1, k), 0
            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + func(i + 1, k - j - 1))
            return res

        return func(0, k)


