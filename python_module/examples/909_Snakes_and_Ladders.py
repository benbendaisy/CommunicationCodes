from collections import deque
from typing import List


class Solution:
    """
        You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

        You start on square 1 of the board. In each move, starting from square curr, do the following:

        Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
        This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
        If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
        The game ends when you reach the square n2.
        A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

        Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

        For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
        Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

        Example 1:

        Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
        Output: 4
        Explanation:
        In the beginning, you start at square 1 (at row 5, column 0).
        You decide to move to square 2 and must take the ladder to square 15.
        You then decide to move to square 17 and must take the snake to square 13.
        You then decide to move to square 14 and must take the ladder to square 35.
        You then decide to move to square 36, ending the game.
        This is the lowest possible number of moves to reach the last square, so return 4.
        Example 2:

        Input: board = [[-1,-1],[-1,3]]
        Output: 1
    """
    def snakesAndLadders1(self, board: List[List[int]]) -> int:
        visited = {1}
        n_board = []
        q = [(1, 0)]
        n = len(board)
        '''this loop is to rearrange the board in 2D manner'''
        for i in range(n - 1, -1, -1):
            if i % 2 != n % 2:
                for j in range(n):
                    n_board.append(board[i][j])
            else:
                for j in range(n - 1, -1, -1):
                    n_board.append(board[i][j])
        #BFS
        while q:
            a = q.pop(0)
            for i in range(6):
                try:
                    if n_board[a[0] + i] == -1:
                        t = a[0] + i + 1
                    else:
                        t = n_board[a[0] + i]
                except:
                    break
                if t in visited:
                    continue
                visited.add(t)
                if t == n ** 2:
                    return a[1] + 1
                q.append((t, a[1] + 1))
        return -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, level = len(board), 0
        line = [0] # unfold matrix to line, dummy 0 for position 0
        for row in range(n)[::-1]:
            line.extend(board[row] if (n - row) % 2 else board[row][::-1])
        que, visited, target = deque([1]), set(), n ** 2
        next_options = lambda x: range(x + 1, min(x + 6, target) + 1)
        while que:
            level += 1
            for _ in range(len(que)):
                cur = que.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                for next in next_options(cur):
                    if line[next] != -1:
                        next = line[next]
                    if next == target:
                        return level
                    que.append(next)
        return -1



