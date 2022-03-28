from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        cnt: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    self.floodFill(grid, i, j)
        return cnt


    def floodFill(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.floodFill(grid, i + 1, j)
        self.floodFill(grid, i - 1, j)
        self.floodFill(grid, i, j + 1)
        self.floodFill(grid, i, j - 1)

if __name__ == "__main__":
    metric = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    solution = Solution()
    ret = solution.numIslands(metric)
    print(ret)