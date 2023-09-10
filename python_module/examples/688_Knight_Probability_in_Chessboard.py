from collections import defaultdict


class Solution:
    """
    On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

    A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

    Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

    The knight continues moving until it has made exactly k moves or has moved off the chessboard.

    Return the probability that the knight remains on the board after it has stopped moving.

    Example 1:

    Input: n = 3, k = 2, row = 0, column = 0
    Output: 0.06250
    Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
    From each of those positions, there are also two moves that will keep the knight on the board.
    The total probability the knight stays on the board is 0.0625.
    Example 2:

    Input: n = 1, k = 0, row = 0, column = 0
    Output: 1.00000
    """
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        adj_list = defaultdict(list)
        directions = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2))
        # find all the moves for a given position
        for r in range(n):
            for col in range(n):
                for dx, dy in directions:
                    new_pos = (r + dx, col + dy)
                    if 0 <= new_pos[0] < n and 0 <= new_pos[1] < n:
                        adj_list[(r, col)].append(new_pos)
        @lru_cache(None)
        def get_leafs_num(pos, h):
            """count all the possible moves for a position in h steps"""
            if h == k:
                return 1
            res = 0
            for next_pos in adj_list[pos]:
                res += get_leafs_num(next_pos, h + 1)
            return res
        leafs_num = get_leafs_num((row, column), 0)
        # there are 8 ** k possible moves for k steps
        return leafs_num / (8**k)