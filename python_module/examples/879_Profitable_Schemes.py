from typing import List


class Solution:
    """
        There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

        Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

        Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

        Example 1:

        Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
        Output: 2
        Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
        In total, there are 2 schemes.
        Example 2:

        Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
        Output: 7
        Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
        There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
    """
    def profitableSchemes1(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        Mod = 10 ** 9 + 7
        dp = [[0] * (n + 1) for i in range(minProfit + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(i + p, minProfit)][j + g] += dp[i][j]
                    dp[min(i + p, minProfit)][j + g] %= Mod
        return sum(dp[minProfit]) % Mod
    
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        @cache
        def helper(idx: int, members: int, pro: int) -> int:
            if idx == len(profit):
                return 1 if pro >= minProfit else 0
            
            #do not comit that task
            num_ways = helper(idx + 1, members, pro)
            if members + group[idx] <= n:
                # use min to guarantee the profit does not exceed minProfit, which save memory
                num_ways += helper(idx + 1, members + group[idx], min(pro + profit[idx], minProfit))
            return num_ways % mod
        
        return helper(0, 0, 0) % mod