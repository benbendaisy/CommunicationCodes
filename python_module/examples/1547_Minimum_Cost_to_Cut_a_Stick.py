from typing import List


class Solution:
    """
    Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:

    Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

    You should perform the cuts in order, you can change the order of the cuts as you wish.

    The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

    Return the minimum total cost of the cuts.

    Example 1:

    Input: n = 7, cuts = [1,3,4,5]
    Output: 16
    Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:

    The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
    Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).
    Example 2:

    Input: n = 9, cuts = [5,6,1,4,2]
    Output: 22
    Explanation: If you try the given cuts ordering the cost will be 25.
    There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
    """
    def minCost0(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()
        @lru_cache(None)
        def dfs(lo, up):
            if lo + 1 == up:
                return 0
            return cuts[up] - cuts[lo] + min(dfs(lo, k) + dfs(k, up) for k in range(lo + 1, up))
        return dfs(0, len(cuts) - 1)
    
    def minCost1(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()
        n = len(cuts)
        dp = [[0] * n for _ in cuts]
        for i in reversed(range(n)):
            for j in range(i + 2, n):
                dp[i][j] = cuts[j] - cuts[i] + min(dp[i][k] + dp[k][j] for k in range(i + 1, j))
        return dp[0][-1]
    
    def minCost2(self, n: int, cuts: List[int]) -> int:
        if not cuts:
            return 0  # If no cuts, cost is 0
        
        cuts.extend([0, n])
        cuts.sort()
        
        @lru_cache(None)
        def helper(left, right):
            if right - left == 1:
                return 0  # No space to cut
            
            min_cost = float('inf')
            for i in range(left + 1, right):
                cost = cuts[right] - cuts[left] + helper(left, i) + helper(i, right)
                min_cost = min(min_cost, cost)
            
            return min_cost if min_cost != float('inf') else 0
        
        return helper(0, len(cuts) - 1)
    
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        @cache
        def helper(left, right):
            if left > right:
                return 0
            
            res = helper(left, right - 1) + 1  # Printing s[right] separately
            
            for i in range(left, right):
                if s[i] == s[right]:  # Try merging prints
                    res = min(res, helper(left, i) + helper(i + 1, right - 1))
            
            return res
        
        return helper(0, n - 1)