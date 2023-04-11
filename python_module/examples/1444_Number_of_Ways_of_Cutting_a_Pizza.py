from functools import lru_cache
from typing import List


class Solution:
    """
        Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts.

        For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

        Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

        Example 1:

        Input: pizza = ["A..","AAA","..."], k = 3
        Output: 3
        Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
        Example 2:

        Input: pizza = ["A..","AA.","..."], k = 3
        Output: 1
        Example 3:

        Input: pizza = ["A..","A..","..."], k = 1
        Output: 1
    """
    def ways(self, pizza: List[str], k: int) -> int:
        @lru_cache(None)
        def has_apple(start_row, start_col, end_row, end_col):
            for r in range(start_row, end_row + 1):
                for c in range(start_col, end_col + 1):
                    if pizza[r][c] == "A":
                        return True
            return False

        @lru_cache(None)
        def dp(start_row, start_col, num_slices_left):
            if num_slices_left == 1:
                if has_apple(start_row, start_col, len(pizza) - 1, len(pizza[0]) - 1):
                    return 1
            num_ways = 0
            for i in range(start_col + 1, len(pizza[0])):
                if has_apple(start_row, start_col, len(pizza) - 1, i - 1):
                    num_ways += dp(start_row, i, num_slices_left - 1)
            for j in range(start_row + 1, len(pizza)):
                if has_apple(start_row, start_col, j - 1, len(pizza[0]) - 1):
                    num_ways += dp(j, start_col, num_slices_left - 1)
            return num_ways
        return dp(0, 0, k) % (10 ** 9 + 7)

