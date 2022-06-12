from functools import lru_cache


class Solution:
    """
        You are playing the following Nim Game with your friend:

        Initially, there is a heap of stones on the table.
        You and your friend will alternate taking turns, and you go first.
        On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
        The one who removes the last stone is the winner.
        Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

        Example 1:

        Input: n = 4
        Output: false
        Explanation: These are the possible outcomes:
        1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
        2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
        3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
        In all outcomes, your friend wins.
        Example 2:

        Input: n = 1
        Output: true
        Example 3:

        Input: n = 2
        Output: true

        Constraints:

        1 <= n <= 231 - 1
    """
    @lru_cache(None)
    def canWinNim1(self, n: int) -> bool:
        if 0 < n <= 3:
            return True
        elif n <= 0:
            return False

        for i in range(1, 4):
            if not self.canWinNim(n - i):
                return True
        return False

    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True

        return not self.canWinNim(n - 1) or \
               not self.canWinNim(n - 2) or \
               not self.canWinNim(n - 3)