import math
from typing import List


class Solution:
    def minCostII1(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs[0])
        dp = [0] * n
        length = len(costs)
        for i in range(length):
            localDP = dp.copy()
            for j in range(n):
                if j == 0:
                    localDP[j] = min(dp[1:]) + costs[i][j]
                elif j == n - 1:
                    localDP[j] = min(dp[:n-1]) + costs[i][j]
                else:
                    localDP[j] = min(min(dp[:j]), min(dp[j + 1:])) + costs[i][j]

            dp = localDP
        return min(dp)
    
    def minCostII2(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        k = len(costs[0])
        dp = [0] * k
        n = len(costs)

        for cost in costs:
            local_dp = dp.copy()
            for i in range(k):
                if i == 0:
                    local_dp[i] = min(dp[i + 1:]) + cost[i]
                elif i == k - 1:
                    local_dp[i] = min(dp[:i]) + cost[i]
                else:
                    local_dp[i] = min(min(dp[:i]), min(dp[i + 1:])) + cost[i]
            dp = local_dp
        
        return min(dp)
    
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        k = len(costs[0])
        dp = [0] * k
        n = len(costs)

        for cost in costs:
            min1, min2 = float('inf'), float('inf')
            for val in dp:
                if val < min1:
                    min2 = min1
                    min1 = val 
                elif val < min2:
                    min2 = val

            for i in range(k):
                dp[i] = (min1 if dp[i] != min1 else min2) + cost[i]
        return min(dp)

if __name__ == "__main__":
    costs = [[1,5,3],[2,9,4]]
    solution = Solution()
    ret = solution.minCostII(costs)
    print(ret)