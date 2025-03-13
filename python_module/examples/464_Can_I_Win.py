from functools import lru_cache


class Solution:
    """
        In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

        What if we change the game so that players cannot re-use integers?

        For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

        Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

        Example 1:

        Input: maxChoosableInteger = 10, desiredTotal = 11
        Output: false
        Explanation:
        No matter which integer the first player choose, the first player will lose.
        The first player can choose an integer from 1 up to 10.
        If the first player choose 1, the second player can only choose integers from 2 up to 10.
        The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
        Same with other integers chosen by the first player, the second player will always win.
        Example 2:

        Input: maxChoosableInteger = 10, desiredTotal = 0
        Output: true
        Example 3:

        Input: maxChoosableInteger = 10, desiredTotal = 1
        Output: true
    """
    def canIWin1(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        takens = [False] * (maxChoosableInteger + 1)

        @lru_cache(None)
        def can_i_win(current_total: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                if not takens[i]:
                    if current_total + i >= desiredTotal:
                        return True
                    takens[i] = True
                    if not can_i_win(current_total + i):
                        return True
                    takens[i] = False
            return False
        if desiredTotal == 0:
            return True
        if sum([i for i in range(1, maxChoosableInteger + 1)]) < desiredTotal:
            return False
        return can_i_win(0)

    def canIWin2(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
        if sum([i for i in range(1, maxChoosableInteger + 1)]) < desiredTotal:
            return False
        def can_i_win(left_total, bit_mask):
            if left_total <= 0 and bit_mask:
                return False

            for i in range(maxChoosableInteger):
                if not (bit_mask >> i) & 1: # check if the ith num is taken
                    if not can_i_win(left_total - i - 1, bit_mask | 1 << i):
                        return True
        return can_i_win(desiredTotal, 0)
    
    def canIWin3(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False  # If sum of all numbers is less than desiredTotal, no one can win.

        @cache
        def helper(remaining: int, mask: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                if mask & (1 << i) == 0:
                    # If choosing i makes us reach or exceed the remaining total, we win
                    if remaining - i <= 0 or not helper(remaining - i, mask | (1 << i)):
                        return True
            return False

        return helper(desiredTotal, 0)
    
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        @cache
        def helper(remaining: int, mask: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                if mask & (1 << i) == 0 and (remaining <= i or not helper(remaining - i, mask | (1 << i))):
                    return True
            return False
        
        return helper(desiredTotal, 0)



if __name__ == "__main__":
    solution = Solution()
    ret = solution.canIWin(10, 40)
    print(ret)