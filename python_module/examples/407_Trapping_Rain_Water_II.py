import heapq
from typing import List


class Solution:
    """
        Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

        Example 1:

        Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
        Output: 4
        Explanation: After the rain, water is trapped between the blocks.
        We have two small ponds 1 and 3 units trapped.
        The total volume of water trapped is 4.
        Example 2:

        Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
        Output: 10
    """
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # number of rows
        m = len(heightMap)
        # number of columns
        n = len(heightMap[0])
        #initialize visited nodes and heapq
        flag = [[0 for _ in range(n)] for _ in range(m)]
        minHeap = []
        for i in range(m):
            for j in range(n):
                # first add to the minheap the border of the enclosed rain water area
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    # push into the heap (height, i,j) since we need to know the index of each height for later
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                else:
                    # mark the grid unvisited
                    flag[i][j] = 1
        #directional vector
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        while minHeap:
            # the height of the water is determined by the lowest point in the border
            curr = heapq.heappop(minHeap)
            for dx, dy in directions:
                newX = curr[1] + dx
                newY = curr[2] + dy
                # check out of bound condition or if the node is already visited
                if newX < 0 or newX >= m or newY < 0 or newY >= n or flag[newX][newY] == 0:
                    continue
                # if the new location has a smaller height than the current one (being popped), then it can at least accumulate as much rain water as the current location
                if heightMap[newX][newY] <= curr[0]:
                    #update the new border with new height (after accumulating water)
                    heapq.heappush(minHeap, (curr[0], newX, newY))
                else:
                    heapq.heappush(minHeap, (heightMap[newX][newY], newX, newY))
                #mark the visited node
                flag[newX][newY] = 0
                ans += max(0, curr[0] - heightMap[newX][newY])
        return ans

