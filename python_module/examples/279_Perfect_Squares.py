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
    def numSquares0(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]

        dp = [math.inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]

    def numSquares1(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]

        @lru_cache(None)
        def squares(k: int) -> int:
            if k in square_nums:
                return 1

            min_square = math.inf
            for square in square_nums:
                if k < square:
                    break
                min_square = min(min_square, squares(k - square) + 1)
            return min_square

        return squares(n)

    def numSquares2(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
        @cache
        def helper(k):
            if k in square_nums:
                return 1
            min_num = float('inf')
            for square in square_nums:
                if k < square:
                    break
                new_num = helper(k - square) + 1
                min_num = min(min_num, new_num)
            return min_num
        return helper(n)
    
    def numSquares3(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]
        
        @cache
        def helper(sum_cnt: int):
            if sum_cnt == n:
                return 0
            
            min_nums = float('inf')
            for i in range(0, len(squares)):
                t = sum_cnt + squares[i]
                if t <= n:
                    min_nums = min(min_nums, 1 + helper(t))
            return min_nums
        
        return helper(0)
    
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]

        @cache
        def helper(cur_sum: int):
            if cur_sum == n:
                return 0

            min_nums = float('inf')
            for square in squares:
                t = cur_sum + square
                if t <= n:
                    min_nums = min(min_nums, 1 + helper(t))
            return min_nums
        
        return helper(0)