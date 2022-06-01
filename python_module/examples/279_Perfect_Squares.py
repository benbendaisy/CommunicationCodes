import math
from cmath import sqrt
from functools import lru_cache


class Solution:
    """
        Given an integer n, return the least number of perfect square numbers that sum to n.

        A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

        Example 1:

        Input: n = 12
        Output: 3
        Explanation: 12 = 4 + 4 + 4.
        Example 2:

        Input: n = 13
        Output: 2
        Explanation: 13 = 4 + 9.


        Constraints:

        1 <= n <= 104
    """
    def numSquares(self, n: int) -> int:
        squareNums = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]

        dp = [math.inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squareNums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]

    def numSquares1(self, n: int) -> int:
        squareNums = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]

        @lru_cache(None)
        def squares(k: int) -> int:
            if k in squareNums:
                return 1

            minSquare = math.inf
            for square in squareNums:
                if square > k:
                    break
                minSquare = min(minSquare, squares(k - square) + 1)
            return minSquare