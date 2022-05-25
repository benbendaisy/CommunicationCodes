import math
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
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

if __name__ == "__main__":
    costs = [[1,5,3],[2,9,4]]
    solution = Solution()
    ret = solution.minCostII(costs)
    print(ret)