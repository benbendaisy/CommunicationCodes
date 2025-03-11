class Solution:
    """
    You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.

    The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

    Return the minimum cost it takes to connect the two groups.

    Example 1:

    Input: cost = [[15, 96], [36, 2]]
    Output: 17
    Explanation: The optimal way of connecting the groups is:
    1--A
    2--B
    This results in a total cost of 17.
    Example 2:

    Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
    Output: 4
    Explanation: The optimal way of connecting the groups is:
    1--A
    2--B
    2--C
    3--A
    This results in a total cost of 4.
    Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.
    Example 3:

    Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
    Output: 10
    """
    def connectTwoGroups1(self, cost: List[List[int]]) -> int:
        size1, size2 = len(cost), len(cost[0])
        
        # Precompute the minimum connection cost for each point in group2
        min_cost_group2 = [min(cost[i][j] for i in range(size1)) for j in range(size2)]
        
        @lru_cache(None)
        def helper(idx: int, mask: int) -> int:
            if idx == size1:  # All points in the first group are processed
                # Ensure all points in group2 are covered at least once
                return sum(min_cost_group2[j] for j in range(size2) if not (mask & (1 << j)))
            
            min_cost = float('inf')
            for j in range(size2):
                new_mask = mask | (1 << j)  # Mark the j-th point in group2 as connected
                min_cost = min(min_cost, cost[idx][j] + helper(idx + 1, new_mask))
            
            return min_cost
        
        return helper(0, 0)
    
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])

        # get the min cost for each column
        min_cost_group = [min(cost[i][j] for i in range(m)) for j in range(n)]
        @cache
        def helper(idx: int, mask: int) -> int:
            if idx == m:
                return sum(min_cost_group[j] for j in range(n) if not ((mask >> j) & 1))
            
            min_cost = float('inf')
            for j in range(n):
                new_mask = mask | (1 << j)
                min_cost = min(min_cost, cost[idx][j] + helper(idx + 1, new_mask))
            return min_cost
        return helper(0, 0)