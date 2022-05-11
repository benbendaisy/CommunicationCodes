from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        dp = [0] * 3

        for cost in costs:
            r = min(dp[1] + cost[0], dp[2] + cost[0])
            g = min(dp[0] + cost[1], dp[2] + cost[1])
            b = min(dp[0] + cost[2], dp[1] + cost[2])
            dp[0], dp[1], dp[2] = r, g, b

        return min(dp)