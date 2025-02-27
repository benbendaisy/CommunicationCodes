from functools import lru_cache
from typing import List


class Solution:
    """
        There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

        A neighborhood is a maximal group of continuous houses that are painted with the same color.

        For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
        Given an array houses, an m x n matrix cost and an integer target where:

        houses[i]: is the color of the house i, and 0 if the house is not painted yet.
        cost[i][j]: is the cost of paint the house i with the color j + 1.
        Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

        Example 1:

        Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
        Output: 9
        Explanation: Paint houses of this way [1,2,2,1,1]
        This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
        Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
        Example 2:

        Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
        Output: 11
        Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
        This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
        Cost of paint the first and last house (10 + 1) = 11.
        Example 3:

        Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
        Output: -1
        Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.

        Constraints:

        m == houses.length == cost.length
        n == cost[i].length
        1 <= m <= 100
        1 <= n <= 20
        1 <= target <= m
        0 <= houses[i] <= n
        1 <= cost[i][j] <= 104
    """
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        maxCnt = 1000001
        @lru_cache(None)
        def findMinCost(hidex: int, neighborcnt: int, prevColor: int):
            if hidex == m:
                return 0 if neighborcnt == target else maxCnt

            if neighborcnt > target:
                return maxCnt

            minCost = maxCnt
            if houses[hidex] == 0:
                for color in range(1, n + 1):
                    newNeighborcnt = neighborcnt + 1 if prevColor != color else neighborcnt
                    minCost = min(minCost, cost[hidex][color - 1] + findMinCost(hidex + 1, newNeighborcnt, color))
            else:
                newNeighborcnt = neighborcnt + 1 if prevColor != houses[hidex] else neighborcnt
                minCost = findMinCost(hidex + 1, newNeighborcnt, houses[hidex])
            return minCost
        minCost = findMinCost(0, 0, -1)
        return minCost if minCost != maxCnt else -1
    
    def minCost(houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = float('inf')

        @lru_cache(None)  # Memoization to avoid recomputation
        def dfs(i, last_color, neighborhoods):
            # Base case: If all houses are painted, check if target is met
            if i == m:
                return 0 if neighborhoods == target else INF
            
            # If we exceed the target, return INF
            if neighborhoods > target:
                return INF

            # If house is already painted, move to the next house
            if houses[i] != 0:
                return dfs(i + 1, houses[i], neighborhoods + (houses[i] != last_color))

            # Try painting with all possible colors and pick the minimum cost
            min_cost = INF
            for c in range(1, n + 1):
                new_neighborhoods = neighborhoods + (c != last_color)
                min_cost = min(min_cost, cost[i][c - 1] + dfs(i + 1, c, new_neighborhoods))
            
            return min_cost

        result = dfs(0, 0, 0)
        return result if result != INF else -1
    
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        inf = float('inf')

        @cache
        def helper(idx: int, last_color: int, neighbor: int):
            if idx == m:
                return 0 if neighbor == target else inf
            
            if neighbor > target:
                return inf
            
            if houses[idx] != 0:
                return helper(idx + 1, houses[idx], neighbor + (houses[idx] != last_color))
            
            min_cost = inf
            for c in range(1, n + 1):
                new_neighbor = neighbor + (c != last_color)
                min_cost = min(min_cost, cost[idx][c - 1] + helper(idx + 1, c, new_neighbor))
            return min_cost
        res = helper(0, 0, 0)
        return res if res != inf else -1