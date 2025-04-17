class Solution:
    """
    Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate k mailboxes in the street.

    Return the minimum total distance between each house and its nearest mailbox.

    The test cases are generated so that the answer fits in a 32-bit integer.

    Example 1:

    Input: houses = [1,4,8,10,20], k = 3
    Output: 5
    Explanation: Allocate mailboxes in position 3, 9 and 20.
    Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
    Example 2:

    Input: houses = [2,3,5,12,18], k = 2
    Output: 9
    Explanation: Allocate mailboxes in position 3 and 14.
    Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
    """
    def minDistance1(self, houses: List[int], k: int) -> int:
        if not houses:
            return -1

        houses.sort()
        n = len(houses)
        # Precompute cost[i][j]: the minimum cost of placing one mailbox for houses[i:j+1]
        cost = [[0] * n for _ in range(n)]
        for left in range(n):
            for right in range(left, n):
                median = houses[(left + right) // 2]
                cost[left][right] = sum([abs(houses[i] - median) for i in range(left, right + 1)])
        
        # Memoization to avoid recomputation
        @cache
        def helper(idx: int, m: int):
            if m == 1: # Base case: Place one mailbox for all remaining houses
                return cost[idx][n - 1]
            
            if idx == n: # No more houses to place mailboxes
                return float('inf')
            
            min_cost = float('inf')
            for i in range(idx, n - m + 1): # Ensure enough houses left for remaining mailboxes
                min_cost = min(min_cost, cost[idx][i] + helper(i + 1, m - 1))
            return min_cost
        
        return helper(0, k)
    
    def minDistance2(self, houses: List[int], k: int) -> int:
        if not houses or len(houses) < k:
            return 0
        n = len(houses)
        houses.sort()
        costs = [[0] * n for _ in range(n)]
        for left in range(n):
            for right in range(n):
                median = (left + right) // 2
                costs[left][right] = sum(abs(houses[k] - houses[median]) for k in range(left, right + 1))

        @cache
        def helper(idx: int, m: int) -> int:
            if m == 1:
                return costs[idx][n - 1]
            
            min_dis = float('inf')
            for i in range(idx, n - m + 1):
                min_dis = min(min_dis, costs[idx][i] + helper(i + 1, m - 1))
            return min_dis
        
        return helper(0, k)