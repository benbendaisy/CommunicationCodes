from collections import deque
from typing import List


class Solution:
    """
        There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

        The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

        The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

        Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

        Example 1:

        Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
        [0,4]: [0,4] -> Pacific Ocean
               [0,4] -> Atlantic Ocean
        [1,3]: [1,3] -> [0,3] -> Pacific Ocean
               [1,3] -> [1,4] -> Atlantic Ocean
        [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
               [1,4] -> Atlantic Ocean
        [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
               [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
        [3,0]: [3,0] -> Pacific Ocean
               [3,0] -> [4,0] -> Atlantic Ocean
        [3,1]: [3,1] -> [3,0] -> Pacific Ocean
               [3,1] -> [4,1] -> Atlantic Ocean
        [4,0]: [4,0] -> Pacific Ocean
               [4,0] -> Atlantic Ocean
        Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
        Example 2:

        Input: heights = [[1]]
        Output: [[0,0]]
        Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

        Constraints:

        m == heights.length
        n == heights[r].length
        1 <= m, n <= 200
        0 <= heights[r][c] <= 105
    """
    def pacificAtlantic1(self, heights: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not heights or not heights[0]:
            return []

        # Initialize variables, including sets used to keep track of visited cells
        m, n = len(heights), len(heights[0])

        # Reversed track from left and top to the cells (pacific)
        # Reversed track from right and bottom to the cells (atlantic)
        pacificReachable, atlanticReachable = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def canFlowToSea(r, c, reachable):
            # This cell is reachable, so mark it
            reachable.add((r, c))
            for dx, dy in directions:
                newR, newC = r + dx, c + dy
                # Check if the new cell is within bounds
                if newR < 0 or newR >= m or newC < 0 or newC >= n:
                    continue
                if (newR, newC) in reachable:
                    continue
                # Check that the new cell has a higher or equal height,
                # So that water can flow from the new cell to the old cell
                if heights[newR][newC] < heights[r][c]:
                    continue
                # If we've gotten this far, that means the new cell is reachable
                canFlowToSea(newR, newC, reachable)

        # Loop through each cell adjacent to the oceans and start a DFS
        for i in range(m):
            canFlowToSea(i, 0, pacificReachable)
            canFlowToSea(i, n - 1, atlanticReachable)

        for j in range(n):
            canFlowToSea(0, j, pacificReachable)
            canFlowToSea(m - 1, j, atlanticReachable)

        return list(pacificReachable.intersection(atlanticReachable))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacificQueue = deque()
        atlanticQueue = deque()
        for i in range(m):
            pacificQueue.append((i, 0))
            atlanticQueue.append((i, n - 1))

        for j in range(n):
            pacificQueue.append((0, j))
            atlanticQueue.append((n - 1, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(queue):
            reachable = set()
            while queue:
                row, col = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))

                for dx, dy in directions:
                    newRow, newCol = row + dx, col + dy
                    # Check if the new cell is within bounds
                    if newRow < 0 or newRow >= m or newCol < 0 or newCol >= n:
                        continue
                    # Check that the new cell hasn't already been visited
                    if (newRow, newCol) in reachable:
                        continue
                    # Check that the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if heights[newRow][newCol] < heights[row][col]:
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((newRow, newCol))
            return reachable

        pacificReachable = bfs(pacificQueue)
        atlanticReachable = bfs(atlanticQueue)
        return list(pacificReachable.intersection(atlanticReachable))