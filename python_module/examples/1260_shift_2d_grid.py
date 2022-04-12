from typing import List


class Solution:
    def shiftOneGrid(self, grid: List[List[int]]):
        m, n = len(grid) - 1, len(grid[0]) - 1
        t = grid[m][n]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if j > 0:
                    grid[i][j] = grid[i][j - 1]
                else:
                    grid[i][j] = grid[i - 1][n]
        grid[0][0] = t

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for i in range(k):
            self.shiftOneGrid(grid)
        return grid

if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    ret = solution.shiftGrid(grid, 1)
    print(ret)